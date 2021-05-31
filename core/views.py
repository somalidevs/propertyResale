from django.shortcuts import render
from .models import *
# Create your views here.






def IndexView(request):
    return render(request,'index.html',{})


def PackageView(request):
    package = Plan.objects.all()
    return render(request,'package.html',{'package':package})


def PackageViewDetail(self,slug):
    package = Plan.objects.get(slug=slug)
    return render(request,'package_detail.html',{'package':package})