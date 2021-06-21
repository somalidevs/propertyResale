from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from .forms import *
from accounts.models import Customer

from .filters import CustomerFilter
from django import template
from django.conf import settings
import stripe
from django.http import JsonResponse
# register = template.Library()
from django.views import generic

def IndexView(request):
    return render(request,'index.html',{})


def PackageView(request):
    package = Plan.objects.all()
    return render(request,'package.html',{'packages':package})


def PackageViewDetail(request,slug):
    # try:
        package = Plan.objects.get(slug=slug)
        user = request.user.customer
        users = request.user
        # cu_objects = Customer(instance=user)
        bank_name = request.POST.get('bank_name')
        account = request.POST.get('account')
        if request.POST:
            en = EnquiryPlan(plan=package,user=user,bank_name=bank_name,account=account)      
            en.save()    
            cu_obj = Customer.objects.filter(user=users).first()
            if cu_obj:
                cu_obj.role="seller"
                cu_obj.save()
                return redirect('/Success-transaction')
    # except:
    #     return render(request,'500.html')
        return render(request,'package_detail.html',{'package':package})


def Success(request):
    return render(request,'success.html',{})

    
def TermsConditions(request):
    return render(request,'terms-condition.html',{})
    

def BankAccounts(request):
    return render(request,'banks.html',{})


# CUSTOMER SECTION

def CustomerView(request):
    customer = Customer.objects.all()
    filtered_customer = CustomerFilter(request.GET,queryset=customer)
    customer = filtered_customer.qs
    return render(request,'customers.html',{'customers':customer,'filter':filtered_customer})


def CustomerDetailView(request,slug):
    customer = Customer.objects.get(slug=slug)
    return render(request,'customers_detail.html',{'customer':customer})

def CustomerEditView(request,slug):
    customer = Customer.objects.get(slug=slug)
    form = CustomerEditForm(request.POST or None,instance=customer)
    if request.POST:    
        customer = Customer.objects.get(slug=slug)
        form = CustomerEditForm(request.POST or None,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('../../customers/admin')
        else:
            messages.error(request,'Oops Something Went Wrong')
    return render(request,'customer_edit.html',{'form':form,'customer':customer})

# ENDCUSTOMER SECTION







# PROFILE SECTION
def ProfileView(request):
    user = request.user.customer
    enquiry = EnquiryPlan.objects.filter(user=user)
    plan = Plan.objects.get(name='Free Trial')
    plan1 = Plan.objects.get(name='Standard Package')
    plan2= Plan.objects.get(name='Premium Package')
    plan3 = Plan.objects.get(name='Basic Package')
    sub = Subscription.objects.filter(user=user,plan=plan)
    sub1 = Subscription.objects.filter(user=user,plan=plan1)
    sub2 =Subscription.objects.filter(user=user,plan=plan2)
    sub3 = Subscription.objects.filter(user=user,plan=plan3)
    
    properti = Property.objects.filter(author=user).count()
    property_data = Property.objects.filter(author=user)
    # if sub and properti >= 1:
    #     return redirect('/')
    context={
        'enquiry':enquiry,
        'sub':sub,
        'sub1':sub1,
        'sub2':sub2,
        'sub3':sub3,
        'properties':property_data,
        
        }

    return render(request,'dashboard_user.html',context)











# END PROFILE SECTION






# START OF STIPE PAYMENT
stripe.api_key = settings.STRIPE_SECRET_KEY


def StripePayment(request,slug):
    public_key = settings.STRIPE_PUBLIC_KEY
    plan = Plan.objects.get(slug=slug)
    context ={'STRIPE_PUBLIC_KEY':public_key,'slug':plan}
    return render(request,'payment.html',context)

# class PaymentView(generic.TemplateView):
    
#     template_name='payment.html'
    
#     def get_context_data(self, **kwargs):
#         context = super(PaymentView,self).get_context_data(**kwargs)
#         context.update({'STRIPE_PUBLIC_KEY':settings.STRIPE_PUBLIC_KEY})
    
#         return context    
    
    
    
def createSubscription(request):
    if request.POST:
        data = request.post
        cusotmer_id = request.user.customer.stripe_customer_id
        try:
            # Attach the payment method to the customer
            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                cusotmer_id,
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                cusotmer_id,
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            # Create the subscription
            subscription = stripe.Subscription.create(
                customer=cusotmer_id,
                items=[{'price': data["priceId"]}],
                expand=['latest_invoice.payment_intent'],
            )
            data ={}
            data.update(subscription)
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'error':{'message': str(e)}})



def retrySubscription(request):
    if request.POST:
        data = request.post
        cusotmer_id = request.user.customer.stripe_customer_id
        try:

            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=cusotmer_id,
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                cusotmer_id,
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            invoice = stripe.Invoice.retrieve(
                data['invoiceId'],
                expand=['payment_intent'],
            )
            data ={}
            data.update(subscription)
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'error':{'message': str(e)}})
        
# END OF STRIPE PAYMENT







# PROPERTY HANDLING SECTION


def PropertyDisplayView(request):
    category = request.GET.get('category')
    if category == None:
        properti = Property.objects.all()
    elif category:
        properti = Property.objects.filter(category__name=category)
    categories = Category.objects.all()
    location = Location.objects.all()
    p_type = Type.objects.all()
    context={
        'properties':properti,
        'categories':categories,
        'locations':location,
        'types':p_type,
    }
    return render(request,'properties.html',context)




def PropertyDetailView(request,slug):
    properti = Property.objects.get(slug=slug)
    return render(request,'property_detail.html',{'property':properti})
    

def PropertyCreate(request):
    form = CreatePropertyForm(request.POST or None)
    if request.POST:
        form = CreatePropertyForm(request.POST,request.FILES)
        if form.is_valid():
            sr = form.save(commit=False)
            sr.author=request.user.customer
            sr.save()
            messages.success(request,'Successfully Added New Property')
            return redirect('/profile')
    return render(request,'add_property.html',{'form':form})








# END OF PROPERTY HANDLING SECTION