# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-12 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikinciElApp', '0006_auto_20171212_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_addition_log',
            name='product_addition',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='product_sell_log',
            name='product_sell_date',
            field=models.DateField(),
        ),
    ]
