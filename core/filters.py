# import django_filters
from django_filters import DateFilter,CharFilter
from accounts.models import Customer
import django_filters






class CustomerFilter(django_filters.FilterSet):
    fullname = CharFilter(field_name='fullname',lookup_expr='icontains')
    
    # fullname = django_filters.CharFilter(widgets = SelectMultiple(attrs={'class': 'form-control my-2 my-lg-0"'}),field_name="fullname",lookup_expr='icontains')
    class Meta:
        model = Customer
        fields=['fullname','role']





