# Generated by Django 3.2.7 on 2021-09-29 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.BigIntegerField(editable=False)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('title', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.BigIntegerField(editable=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('imageUrl', models.URLField(null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopadmin.product')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopadmin.product')),
            ],
        ),
    ]