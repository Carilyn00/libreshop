# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-16 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fulfillment', '0004_auto_20160411_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fulfillmentsetting',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fulfillment.Supplier'),
        ),
    ]
