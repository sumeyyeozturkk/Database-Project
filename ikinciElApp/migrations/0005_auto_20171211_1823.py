# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-11 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikinciElApp', '0004_auto_20171211_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_addition_log',
            old_name='user_vendor_id',
            new_name='user_seller',
        ),
        migrations.RenameField(
            model_name='product_processing',
            old_name='user_purchaser_id',
            new_name='user_buyer',
        ),
        migrations.RenameField(
            model_name='product_processing',
            old_name='user_vendor_id',
            new_name='user_seller',
        ),
        migrations.RenameField(
            model_name='product_sell_log',
            old_name='user_purchaser_id',
            new_name='user_buyer',
        ),
    ]
