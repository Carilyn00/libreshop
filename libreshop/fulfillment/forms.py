import importlib
import logging
from django import forms
from django.conf import settings
from . import models

# Initialize logger.
logger = logging.getLogger(__name__)

def get_fulfillment_backend_choices():

    fulfillment_backends = []
    for api_name, choice_name in settings.FULFILLMENT_BACKENDS:
        index = api_name.rfind('.')
        module_name, attribute_name = api_name[:index], api_name[index+1:]
        module, attribute = None, None
        try:
            module = importlib.import_module(module_name)
            attribute = getattr(module, attribute_name)
        except ImportError as e:
            logger.critical('Unable to import module \'%s\'.' % module_name)
        except AttributeError as e:
            logger.critical('\'%s\' module has no attribute \'%s\'.' %
                (module_name, attribute_name))
        else:
            fulfillment_backends.append((api_name, choice_name))

    return fulfillment_backends


class SupplierCreationForm(forms.ModelForm):
    class Meta:
        model = models.Supplier
        fields = ('name', 'fulfillment_backend', 'fulfillment_time')

    def __init__(self, *args, **kwargs):
        super(SupplierCreationForm, self).__init__(*args, **kwargs)
        self.fields['fulfillment_backend'] = forms.ChoiceField(
            choices=get_fulfillment_backend_choices
        )
