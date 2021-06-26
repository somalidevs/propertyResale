from django.urls import path,include
from .views import *
urlpatterns = [
    path('',IndexView,name='index_view'),
    path('package/',PackageView,name="package_view"),
    path('package-info/<slug>/payments',PackageViewDetail,name="package_detail"),
    path('terms_conditions',TermsConditions,name='terms_conditions_view'),
    path('banks',BankAccounts,name='bank_account_view',),
    path('Success-transaction',Success,name='success_transaction_view'),
    
    path('admin/customers',CustomerView,name='customers_admin_view'),
    path('admin/customers/<slug>',CustomerDetailView,name='customers_admin_detail_view'),
    path('admin/customers/edit/<slug>',CustomerEditView,name='customers_admin_edit_view'),
    path('admin/customers/delete/<slug>',CustomerDeleteView,name='customers_admin_delete_view'),
    
    path('profile',ProfileView,name='profile_view'),
    path('payments/<slug>',StripePayment,name='payments'),
    
    # PROPERTY URLS
    path('properties',PropertyDisplayView,name='property_view'),
    path('properties-search',PropertyAdvancedSearch,name='property_advanced_search_view'),
    path('property/<slug>',PropertyDetailView,name='property_detail_view'),
    path('property-edit/<slug>',PropertyEditView,name='property_edit_view'),
    
    # CONTACT-US URL
    path('contact-us',ContactUsView,name='contact_us_view'),
]
