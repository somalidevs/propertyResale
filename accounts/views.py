from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from .models import *
from asgiref.sync import sync_to_async
import uuid
from django.conf import settings
from django.core.mail import send_mail
import time
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

from .forms import *

def loginView(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.filter(username=username).first() 
            if user_obj is None:
                messages.error(request,'User not Found')
                return redirect('/login')
            profile_one = Customer.objects.filter(user=user_obj).first()
            if not profile_one.is_verified:
                messages.error(request,'User is not verfied Check your mail')
                return redirect('/login')
            user = authenticate(username=username,password=password)
            if user is None:
                messages.success(request,'Wrong password')
                return redirect('/login')
            login(request,user)
            return redirect('/profile')
        except:
            messages.success(request,'User is not Customer')
            return redirect('/login')
        
    return render(request,'login.html',{})




def LogoutView(request):
    logout(request)
    return redirect('/login')





@sync_to_async
def registerView(request):
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            if User.objects.filter(username=username).first():
                messages.success(request,'This Username is invalid,Pick another one')
                return redirect('/register')

            if User.objects.filter(email=email).first():
                messages.success(request,'This Email is invalid or Taken,Pick another one')
                return redirect('/register')

            user_obj = User(username=username,email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Customer.objects.create(user=user_obj,auth_token=auth_token)
            profile_obj.save()
            send_mail_after_registration(email,username,auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)

    return render(request,'register.html',{})
        



def Verify(request,auth_token):
    try:
        profile_obj = Customer.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            profile_obj.is_verified=True
            profile_obj.save()
            messages.success(request,'You have successfully Verified your account')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
    

def error_page(request):
    return render(request,'404.html')


def tokenSent(request):
    return render(request,'token_send.html',{})


def successToken(request):
    return render(request,'success.html',{})


def send_mail_after_registration(email,username,token):
    subject = 'Your Account Needs to be verified'
    message = f"Hi {username}, please try to paste the link to verify your account http://127.0.0.1:8000/verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)




def UserProfile(request):
    user = request.user.customer
    form = ProfileUpdateForm(request.POST or None,instance=user)

    if request.POST:
        form = ProfileUpdateForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    return render(request,'create_user_profile.html',{'form':form})






