
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginView,name='login_view'),
    path('logout/',LogoutView,name='logout_view'),
    path('register/', registerView,name='register_view'),
    path('token/', tokenSent,name='token_sent'),
    path('success/', successToken,name='success'),
    path('verify/<auth_token>', Verify,name='verify'),
    path('error/', error_page,name='error'),
    path('update-profile',UserProfile,name='update-profile'),
]
