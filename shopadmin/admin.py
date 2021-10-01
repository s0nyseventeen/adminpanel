from django.contrib import admin
from .models import Shop, Product, Order


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('shop_id', 'title', 'imagetoupload', 'date')
	list_filter = ('title','date')
	search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('product_id', 'title', 'amount', 'price', 'active')
	search_fields = ['product_id', 'title']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('shop', 'product', 'date_created', 'status')