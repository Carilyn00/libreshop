# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-18 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfillment', '0009_shipment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='tracking_number',
        ),
        migrations.AddField(
            model_name='shipment',
            name='tracking_id',
            field=models.CharField(default='12345', max_length=64, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shipment',
            name='carrier',
            field=models.CharField(max_length=32),
        ),
    ]
