# Generated by Django 3.2.7 on 2021-09-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopadmin', '0006_shop_imagetoupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop_id',
            field=models.IntegerField(default=0),
        ),
    ]
