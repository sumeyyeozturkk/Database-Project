# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-12 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikinciElApp', '0007_auto_20171212_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_addition_log',
            name='product_addition',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='product_sell_log',
            name='product_sell_date',
            field=models.DateTimeField(),
        ),
    ]