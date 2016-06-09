# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-28 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160417_1957'),
        ('fulfillment', '0006_auto_20160513_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='fulfillmentsettingvalue',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='fulfillmentsettingvalue',
            unique_together=set([('setting', 'variant'), ('setting', 'product')]),
        ),
    ]