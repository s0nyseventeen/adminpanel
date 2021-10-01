# Generated by Django 3.2.7 on 2021-09-29 21:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shopadmin', '0004_auto_20210930_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
    ]