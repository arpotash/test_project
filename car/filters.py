from django_filters import rest_framework as filters
from .models import Organization, Car


class OrganizationNameFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Organization
        fields = ['name', 'country']


class CarFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Car
        fields = ['diller', 'min_price', 'max_price']
