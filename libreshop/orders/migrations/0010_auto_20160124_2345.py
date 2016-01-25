# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-24 23:45
from __future__ import unicode_literals

from django.db import migrations, models
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_fulfilled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='token',
            field=models.CharField(default=orders.models.get_token, max_length=8, unique=True),
        ),
    ]
