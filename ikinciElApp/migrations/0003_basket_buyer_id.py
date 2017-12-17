# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-11 16:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ikinciElApp', '0002_product_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='buyer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
