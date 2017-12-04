# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('city', models.TextField()),
                ('street', models.TextField()),
                ('neighborhood', models.TextField()),
                ('gate_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('basket_addition_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('brand_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('product_picture', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('product_status', models.BooleanField(default=False)),
                ('product_brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ikinciElApp.Brand')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ikinciElApp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product_addition_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('product_addition', models.DateTimeField(default=django.utils.timezone.now)),
                ('explanation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product_processing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('product_id', models.ForeignKey(default=0, to='ikinciElApp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_sell_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('product_sell_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('explanation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, default=1, serialize=False, related_name='Profile', to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('e_mail', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=11)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('gender', models.NullBooleanField(choices=[(True, 'Male'), (False, 'Female')])),
                ('address_id', models.ForeignKey(blank=True, null=True, to='ikinciElApp.Address')),
                ('basket_id', models.OneToOneField(blank=True, null=True, to='ikinciElApp.Basket')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('role_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='product_sell_log',
            name='user_purchaser_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product_processing',
            name='user_purchaser_id',
            field=models.OneToOneField(related_name='alici_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product_processing',
            name='user_vendor_id',
            field=models.OneToOneField(related_name='satici_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product_addition_log',
            name='user_vendor_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='basket',
            name='product_id',
            field=models.ForeignKey(to='ikinciElApp.Product'),
        ),
    ]
