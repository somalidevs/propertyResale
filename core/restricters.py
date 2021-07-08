from django.shortcuts import redirect
from django.http import HttpResponse


def unathenticated_user(view_func):
    def checking_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args, **kwargs)
        
    return checking_func



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def checking_func(request,*args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse('YOu are not allowed here')


        return checking_func
    return decorator
        


def admin_only(view_func):
    def checking_func(request,*args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group =='customer':
            return redirect('user_page')
        elif group == 'admin':
            return view_func(request,*args, **kwargs)
        else:
            return redirect('login')
        
    return checking_func