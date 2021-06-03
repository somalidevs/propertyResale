from django.urls import path,include
from .views import *
urlpatterns = [
    path('',IndexView,name='index_view'),
    path('package/',PackageView,name="package_view"),
    path('package-info/<slug>',PackageViewDetail,name="package_detail"),
    path('terms-conditions',TermsConditions,name='terms_conditions_view'),
    path('banks',BankAccounts,name='bank_account_view',),
    path('Success-transaction',Success,name='success_transaction_view'),
    path('customers/admin',CustomerView,name='customers_admin_view'),
    path('customers/admin/<slug>',CustomerDetailView,name='customers_admin_detail_view'),
    path('customers/admin/edit/<slug>',CustomerEditView,name='customers_admin_edit_view'),
    path('profile',ProfileView,name='profile_view'),
]
