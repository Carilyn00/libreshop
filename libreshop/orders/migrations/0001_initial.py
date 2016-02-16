# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 14:52
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0002_customer_selected_products'),
        ('products', '0001_initial'),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('token', models.CharField(default=orders.models.get_token, max_length=8, unique=True)),
                ('fulfilled', models.BooleanField(default=False)),
                ('subtotal', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('sales_tax', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses.Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Variant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaxRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('state', models.CharField(blank=True, max_length=4, null=True)),
                ('district', models.CharField(blank=True, max_length=4, null=True)),
                ('county', models.CharField(blank=True, max_length=4, null=True)),
                ('city', models.CharField(blank=True, max_length=4, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=16, null=True)),
                ('state_tax_rate', models.DecimalField(decimal_places=4, default=Decimal('0.00'), max_digits=5)),
                ('district_tax_rate', models.DecimalField(decimal_places=4, default=Decimal('0.00'), max_digits=5)),
                ('county_tax_rate', models.DecimalField(decimal_places=4, default=Decimal('0.00'), max_digits=5)),
                ('local_tax_rate', models.DecimalField(decimal_places=4, default=Decimal('0.00'), max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
