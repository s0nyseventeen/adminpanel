from django.db import models


class Shop(models.Model):
	shop_id = models.IntegerField(default=0, editable=False)
	title = models.CharField(max_length=50)
	description = models.TextField(max_length=1000, null=True)
	imageUrl = models.URLField(max_length=200, null=True)
	date = models.DateField(auto_now_add=True, null=True)
	imagetoupload = models.ImageField(upload_to='images', null=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.shop_id += 1
		super().save(*args, **kwargs)


class Product(models.Model):
	product_id = models.IntegerField(default=0, editable=False)
	description = models.TextField(max_length=1000, null=True)
	title = models.CharField(max_length=50)
	amount = models.IntegerField(default=0)
	price = models.FloatField(default=0, null=True)
	active = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.product_id += 1
		super().save(*args, **kwargs)


class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Out for delivery', 'Out for delivery'),
		('Delivered', 'Delivered')	
	)
	shop = models.ForeignKey(Shop, null=True,
							 on_delete=models.SET_NULL)
	product = models.ForeignKey(Product, null=True,
								on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.product.title


class Images(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.URLField(max_length=200, null=True)
