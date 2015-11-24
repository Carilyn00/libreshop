# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-24 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0007_remove_address_customer'),
        ('customers', '0002_customer_selected_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='addresses',
            field=models.ManyToManyField(blank=True, to='addresses.Address'),
        ),
    ]
