# import django_filters
from core.models import Property
from django_filters import DateFilter,CharFilter
from accounts.models import Customer
import django_filters






class CustomerFilter(django_filters.FilterSet):
    fullname = CharFilter(field_name='fullname',lookup_expr='icontains')
    
    # fullname = django_filters.CharFilter(widgets = SelectMultiple(attrs={'class': 'form-control my-2 my-lg-0"'}),field_name="fullname",lookup_expr='icontains')
    class Meta:
        model = Customer
        fields=['fullname','role']





class PropertyFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains')
    
    # fullname = django_filters.CharFilter(widgets = SelectMultiple(attrs={'class': 'form-control my-2 my-lg-0"'}),field_name="fullname",lookup_expr='icontains')
    class Meta:
        model = Property
        fields=['name','category','location','ptype']