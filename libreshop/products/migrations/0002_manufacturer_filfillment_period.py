# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-08 04:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='filfillment_period',
            field=models.DurationField(default=datetime.timedelta(0), help_text='Specify time delta in [DD] [HH:[MM:]]ss[.uuuuuu] format.'),
        ),
    ]
