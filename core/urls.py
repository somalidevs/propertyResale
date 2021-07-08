from django.urls import path,include
from .views import *
urlpatterns = [
    path('',IndexView,name='index_view'),
    path('package/',PackageView,name="package_view"),
    path('package-info/<slug>/payments',PackageViewDetail,name="package_detail"),
    path('terms_conditions',TermsConditions,name='terms_conditions_view'),
    path('banks',BankAccounts,name='bank_account_view',), 
    path('Success-transaction',OnSubscriptionComplete,name='success_transaction_view'),
    
    # admin urls
    path('admin/customers',adminCustomerView,name='admin_customers_view'),
    path('admin/customers/<slug>',adminCustomerDetailView,name='customers_admin_detail_view'),
    path('admin/customers/edit/<slug>',adminCustomerEditView,name='customers_admin_edit_view'),
    path('admin/customers/delete/<slug>',adminCustomerDeleteView,name='customers_admin_delete_view'),
    path('admin/properties',adminPropertiesView,name="admin_properties_view"),
    path('admin/subscriptions',adminSubscriptions,name="admin_subscriptions_view"),
    
    
    path('profile',ProfileView,name='profile_view'),
    path('payments/<slug>',StripePayment,name='payments'),
    path('create-subscription',CreateSubscriptionView.as_view(),name="create_subscription_view"),
    path('retry-subscription',RetrySubscription,name="retry_subscription_view"),
    
    # PROPERTY URLS
    path('properties',PropertyDisplayView,name='property_view'),
    path('properties-search',PropertyAdvancedSearch,name='property_advanced_search_view'),
    path('property/<slug>',PropertyDetailView,name='property_detail_view'),
    path('property-edit/<slug>',PropertyEditView,name='property_edit_view'),
    path('property-delete/<slug>',PropertyDeleteView,name='property_delete_view'),
    
    # CONTACT-US URL
    path('contact-us',ContactUsView,name='contact_us_view'),
]
