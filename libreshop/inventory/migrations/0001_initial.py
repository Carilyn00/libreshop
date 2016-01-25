# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 13:48
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attribute_Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('value', models.CharField(max_length=64)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Attribute')),
            ],
            options={
                'verbose_name': 'attribute',
                'verbose_name_plural': 'attributes',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=64)),
                ('cost', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('alternatives', models.ManyToManyField(blank=True, related_name='_inventory_alternatives_+', to='inventory.Inventory')),
                ('attributes', models.ManyToManyField(through='inventory.Attribute_Value', to='inventory.Attribute')),
            ],
            options={
                'verbose_name_plural': 'inventory',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addresses.Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='location',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Warehouse'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='warehouses',
            field=models.ManyToManyField(through='inventory.Location', to='inventory.Warehouse'),
        ),
        migrations.AddField(
            model_name='attribute_value',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Inventory'),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('inventory', 'warehouse')]),
        ),
        migrations.AlterUniqueTogether(
            name='attribute_value',
            unique_together=set([('inventory', 'attribute')]),
        ),
    ]
