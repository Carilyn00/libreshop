# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('recipient_name', models.CharField(blank=True, max_length=64, null=True)),
                ('street_address', models.CharField(max_length=1024)),
                ('locality', models.CharField(max_length=16)),
                ('region', models.CharField(max_length=16)),
                ('postal_code', models.CharField(blank=True, max_length=16, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
    ]
