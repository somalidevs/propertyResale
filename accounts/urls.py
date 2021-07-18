
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', loginView,name='login_view'),
    path('logout/',LogoutView,name='logout_view'),
    path('removeaccount/',remove_account,name='remove_account_view'),
    path('register/', registerView,name='register_view'),
    path('token/', tokenSent,name='token_sent'),
    path('success/', successToken,name='success'),
    path('verify/<auth_token>', Verify,name='verify'),
    path('error/', error_page,name='error'),
    path('update-profile',UserProfile,name='update-profile'),
    
    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete"),
]
