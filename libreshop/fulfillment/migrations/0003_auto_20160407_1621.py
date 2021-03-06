# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-07 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fulfillment', '0002_auto_20160407_1621'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fulfillmentpurchase',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Purchase'),
        ),
        migrations.AlterUniqueTogether(
            name='fulfillmentsettingvalue',
            unique_together=set([('setting', 'variant')]),
        ),
        migrations.AlterUniqueTogether(
            name='fulfillmentsetting',
            unique_together=set([('supplier', 'name')]),
        ),
    ]
