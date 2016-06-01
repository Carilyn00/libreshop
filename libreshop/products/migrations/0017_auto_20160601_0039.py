# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-01 00:39
from __future__ import unicode_literals

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20160601_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Point of Interest'),
        ),
    ]
