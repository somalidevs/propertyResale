from django.contrib import messages
from django.core import paginator
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from .forms import *
from accounts.models import Customer

from asgiref.sync import sync_to_async

from django.urls import reverse
from django.http import HttpResponseRedirect

from django.core.mail import send_mail

from .filters import CustomerFilter
from django import template
from django.conf import settings
import stripe
from django.http import JsonResponse
# register = template.Library()
from django.views import generic
from django.core.paginator import Paginator
from .filters import *
from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.generic.edit import UpdateView ,DeleteView,CreateView


@sync_to_async
def IndexView(request):
    properti = Property.objects.all().order_by('-id')
    filtered_properti = PropertyFilter(request.GET,queryset=properti)
    properti = filtered_properti.qs
    paginator = Paginator(properti,6)
    page = request.GET.get('q')
    properti = paginator.get_page(page)
    return render(request,'index.html',{'properties':properti,'filter':filtered_properti})


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



    
def TermsConditions(request):
    return render(request,'terms-condition.html',{})
    

def BankAccounts(request):
    return render(request,'banks.html',{})











'''ADMIN SECTION'''


    
def adminCustomerView(request):
    customer = Customer.objects.all()
    filtered_customer = CustomerFilter(request.GET,queryset=customer)
    customer = filtered_customer.qs
    return render(request,'admin_customers.html',{'customers':customer,'filter':filtered_customer})


def adminCustomerDetailView(request,slug):
    customer = Customer.objects.get(slug=slug)
    return render(request,'admin_customers_detail.html',{'customer':customer})

def adminCustomerEditView(request,slug):
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
    return render(request,'admin_customer_edit.html',{'form':form,'customer':customer})




def adminCustomerDeleteView(request,slug):
    r = Customer.objects.get(slug=slug)
    if request.POST:
        r.delete()
        messages.success(request,'Successfully deleted the User')
        return redirect('../../../admin/customers')
    return render(request,'admin_customer_delete.html',{'customer':r})


def adminPropertiesView(request):
    property_data = Property.objects.all()
    page = request.GET.get('q')
    paginator = Paginator(property_data,4)
    property_data = paginator.get_page(page)
    form = CreatePropertyForm(request.POST or None)
    if request.POST:
        form = CreatePropertyForm(request.POST,request.FILES)
        if form.is_valid():
            sr = form.save(commit=False)
            sr.author=request.user.customer
            sr.save()
            messages.success(request,'Successfully Added New Property')
            return redirect('../../admin/properties')
    context ={
        'form':form,
        'properties':property_data,
    }
    return render(request,'admin_properties.html',context)


def adminSubscriptions(request):
    subscription = Subscription.objects.all()
    return render(request,'admin_subscriptions.html',{'sub':subscription})


'''# END aDMIN SECTION'''















'''# PROFILE SECTION'''


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
    property_data = Property.objects.filter(author=user).order_by('-id')
    page = request.GET.get('q')
    paginator = Paginator(property_data,4)
    property_data = paginator.get_page(page)
    form = CreatePropertyForm(request.POST or None)
    if request.POST:
        form = CreatePropertyForm(request.POST,request.FILES)
        if form.is_valid():
            sr = form.save(commit=False)
            sr.author=request.user.customer
            sr.save()
            messages.success(request,'Successfully Added New Property')
            return redirect('/profile')
    # if sub and properti >= 1:
    #     return redirect('/')
    context={
        'enquiry':enquiry,
        'sub':sub,
        'sub1':sub1,
        'sub2':sub2,
        'sub3':sub3,
        'properties':property_data,
        'form':form,
        
        }

    return render(request,'customer_properties.html',context)


'''# END PROFILE SECTION'''






'''# START OF STIPE PAYMENT'''


stripe.api_key = settings.STRIPE_SECRET_KEY
def StripePayment(request,slug):
    public_key = settings.STRIPE_PUBLIC_KEY
    plan = Plan.objects.get(slug=slug)
    context ={'STRIPE_PUBLIC_KEY':public_key,'pricing_tier':plan}
    return render(request,'payment.html',context)

    
    
# def CreateSubscription(request):
#     if request.POST:
#         data = request.post
#         cusotmer_id = request.user.customer.stripe_customer_id
#         try:
#             # Attach the payment method to the customer
#             stripe.PaymentMethod.attach(
#                 data['paymentMethodId'],
#                 cusotmer_id,
#             )
#             # Set the default payment method on the customer
#             stripe.Customer.modify(
#                 cusotmer_id,
#                 invoice_settings={
#                     'default_payment_method': data['paymentMethodId'],
#                 },
#             )

#             # Create the subscription
#             subscription = stripe.Subscription.create(
#                 customer=cusotmer_id,
#                 items=[{'price': data["priceId"]}],
#                 expand=['latest_invoice.payment_intent'],
#             )
#             data ={}
#             data.update(subscription)
#             return JsonResponse(data)
#         except Exception as e:
#             return JsonResponse({'error':{'message': str(e)}})


class CreateSubscriptionView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        customer_id = request.user.customer.stripe_customer_id
        try:
            # Attach the payment method to the customer
            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=customer_id,
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                customer_id,
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            # Create the subscription
            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[{'price': data["priceId"]}],
                expand=['latest_invoice.payment_intent'],
            )

            data = {}
            data.update(subscription)

            return Response(data)
        except Exception as e:
            return Response({
                "error": {'message': str(e)}
            })



def OnSubscriptionComplete(request):
    return render(request,'success.html',{})
    

def RetrySubscription(request):
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
        
'''# END OF STRIPE PAYMENT'''






'''
# PROPERTY HANDLING SECTION'''


def PropertyDisplayView(request):
    category = request.GET.get('category')
    location = request.GET.get('location')
    ptype = request.GET.get('type')
    
    if category == None:
        properti = Property.objects.all()
        
        paginator = Paginator(properti,6)
        page = request.GET.get('q')
        properti = paginator.get_page(page) 
        
    elif category:
        properti = Property.objects.filter(category__name=category)

    if location:
        properti = Property.objects.filter(location__name=location)
    
    if ptype:
        properti = Property.objects.filter(ptype__name=ptype)
        

    categories = Category.objects.all()
    locations = Location.objects.all()
    p_type = Type.objects.all()
    properties_to_be_counted = Property.objects.all().count()
    # p_count = properti.count()
    context={
        'properties':properti,
        'categories':categories,
        'locations':locations,
        'types':p_type,
        'p_count':properties_to_be_counted,
        # 'properties':properties,
        
    }
    return render(request,'properties.html',context)


def PropertyAdvancedSearch(request):
    properti = Property.objects.all()
    # properties = Property.objects.all()
    filtered_properti = PropertyFilter(request.GET,queryset=properti)
    properti = filtered_properti.qs
    paginator = Paginator(properti,6)
    page = request.GET.get('q')
    properti = paginator.get_page(page) 
    context ={
        'properties':properti,
        'filter':filtered_properti,
    }
    return render(request,'advanced_property_search.html',context)

def PropertyDetailView(request,slug):
    properti = Property.objects.get(slug=slug)
    user = request.user.customer
    if request.POST:
        message = request.POST['message']
        enqpr = Enquiry.objects.create(user=user,related_property=properti,message=message)
        enqpr.save()
        messages.success(request,'Successfully submitted your request')
        return HttpResponseRedirect(reverse('property_detail_view',args={str(slug)}))
    return render(request,'property_detail.html',{'property':properti})

def PropertyEditView(request,slug):
    properti = Property.objects.get(slug=slug)
    form = EditPropertyForm(request.POST or None,instance=properti)
    if request.POST:
        form = EditPropertyForm(request.POST or None,request.FILES,instance=properti)
        if form.is_valid():
            slugs = form.save(commit=False)
            form.save()
            messages.success(request,'Property Updated Successfully')
    return render(request,'property_edit.html',{'property':properti,'form':form})

def PropertyDeleteView(request,slug):
    r = Property.objects.get(slug=slug)
    if request.POST:
        r.delete()
        messages.success(request,'Successfully deleted the Property')
        return redirect('/profile')
    return render(request,'property_delete.html',{'property':r})

'''# END OF PROPERTY HANDLING SECTION'''

'''
# CONTACT US SECTION'''






def ContactUsView(request):
    if request.POST:
        username = request.POST['username']
        subject = request.POST['subject']
        email = request.POST['email']
        phone =  request.POST['phone']
        message = request.POST['message']
        msg = ContactUs.objects.create(name=username,subject=subject,email=email,phone=phone,message=message)
        # send_mail(
        #     subject,
        #     message,
        #     email,
        #     ['zaidnajim111@gmail.com'],
        #     fail_silently=True
        # )
        msg.save()
        messages.success(request,'Thank you for contacting Us')
        return redirect('/contact-us')
    
    return render(request,'contact-us.html',{})
    
    
'''# END OF CONTACT US SECTION'''




