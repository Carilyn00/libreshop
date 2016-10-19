# -*- coding: utf-8 -*-

import logging
from django import forms
from .models import Inventory
from .widgets import ConversionFactorField

# Initialize logger
logger = logging.getLogger(__name__)


class InventoryCreationForm(forms.ModelForm):

    purchasing_conversion_factor = ConversionFactorField()

    def __init__(self, *args, **kwargs):
        super(InventoryCreationForm, self).__init__(*args, **kwargs)
        self.fields['alternatives'].queryset = Inventory.objects.exclude(
            pk=self.instance.pk
        )

    class Meta:
        model = Inventory
        fields = ('name', 'alternatives', 'cost', 'weight', 'packed_weight',
            'standard_unit_of_measure', 'purchasing_conversion_factor')
