# Generated by Django 3.2.7 on 2021-10-01 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopadmin', '0008_auto_20210930_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, null=True),
        ),
    ]