from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from .forms import *
from accounts.models import Customer

from .filters import CustomerFilter
from django import template

# register = template.Library()


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
    return render(request,'customer_edit.html',{'form':form,'customer':customer})

# ENDCUSTOMER SECTION







# PROFILE SECTION
def ProfileView(request):
    user = request.user.customer
    enquiry = EnquiryPlan.objects.filter(user=user)
    return render(request,'dashboard_user.html',{'enquiry':enquiry})
# END PROFILE SECTION



