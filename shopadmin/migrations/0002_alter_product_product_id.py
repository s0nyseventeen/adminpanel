# Generated by Django 3.2.7 on 2021-09-29 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.BigIntegerField(editable=False, null=True),
        ),
    ]