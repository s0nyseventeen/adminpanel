from django.shortcuts import render, redirect
from .models import *
from .forms import ShopForm, ProductForm


def home(request):
	shops = Shop.objects.all()
	total_shops = shops.count()
	context = {
		'shops': shops,
		'total_shops': total_shops,
	}
	return render(request, 'shopadmin/shops.html', context)


def products(request):
	products = Product.objects.all()
	total_products = products.count()
	context  = {
		'products': products,
		'total_products': total_products,
	}
	return render(request, 'shopadmin/products.html', context)


def shop_detail(request, pk):
	shop = Shop.objects.get(id=pk)
	orders = shop.order_set.all()
	context = {
		'shop': shop,
		'orders': orders,
	}
	return render(request, 'shopadmin/shop_detail.html', context)


def update_shop(request, pk):
	shop = Shop.objects.get(id=pk)
	form = ShopForm(instance=shop)
	if request.method == 'POST':
		form = ShopForm(request.POST, instance=shop)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
		'form': form
	}
	return render(request, 'shopadmin/orderform_shop.html', context)


def update_product(request, pk):
	product = Product.objects.get(id=pk)
	form = ProductForm(instance=product)
	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
		'form': form
	}
	return render(request, 'shopadmin/orderform_product.html', context)