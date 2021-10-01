from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home'),
	path('products/', products, name='products'),
	path('shop/<int:pk>/', shop_detail, name='shop_detail'),
	path('update_shop/<int:pk>/', update_shop, name='update_shop'),
	path('update_product/<int:pk>/', update_product, name='update_product'),
]