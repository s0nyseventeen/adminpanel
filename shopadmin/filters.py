import django_filters
from .models import *


class ShopFilter(django_filters.FilterSet):
	class Meta:
		model = Shop
		fields = ['title']


class ProductFilter(django_filters.FilterSet):
	class Meta:
		model = Product
		fields = ['product_id', 'title']
