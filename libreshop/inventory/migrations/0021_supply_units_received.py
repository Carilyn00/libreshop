# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 22:52
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0020_auto_20161023_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='units_received',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8),
        ),
    ]
