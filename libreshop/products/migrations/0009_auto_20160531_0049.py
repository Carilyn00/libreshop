# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-31 00:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20160531_0045'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='Image',
        ),
    ]
