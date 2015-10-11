import logging
from django.contrib import admin
from django.contrib.admin.options import IS_POPUP_VAR
from . import models
from .forms import (ProductCreationForm, ProductChangeForm, VariantCreationForm,
    PopulatedFormFactory)
from nested_inline.admin import NestedTabularInline, NestedModelAdmin

# Initialize logger
logger = logging.getLogger(__name__)

# Register your models here.
admin.site.register(models.Component)


class ComponentInlineAdmin(NestedTabularInline):
    model = models.Component
    extra = 0
    show_change_link = False # Does not work with Nested Inlines.


class VariantInlineAdmin(NestedTabularInline):
    model = models.Variant
    inlines = [ComponentInlineAdmin,]
    extra = 0
    show_change_link = False # Does not work with Nested Inlines.

    def get_max_num(self, request, obj=None, **kwargs):
        return models.Variant.objects.filter(product=obj).count() if obj else 1


class ProductAdmin(NestedModelAdmin):

    list_display = ('_sku', 'name')

    form = ProductChangeForm
    add_form = ProductCreationForm

    def _sku(self, instance):
        return instance.sku
    _sku.short_description = 'SKU'
    _sku.admin_order_field = 'sku'

    def get_inline_instances(self, request, obj=None):

        if obj:
            inlines = set(self.inlines)
            inlines = inlines.union({VariantInlineAdmin,})
            self.inlines = list(inlines)
        else:
            self.inlines = []

        return super(ProductAdmin, self).get_inline_instances(request, obj)

    def has_add_permission(self, request):
        """
        Disable 'Add' icon when prepopulating fields.
        """
        if request.method == 'GET' and 'product' in request.GET:
            return False
        else:
            return True

    def has_change_permission(self, request, obj=None):
        """
        Disable 'Edit' icon when prepopulating fields.
        """
        if request.method == 'GET' and 'product' in request.GET:
            return False
        else:
            return True

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during product creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super(ProductAdmin, self).get_form(request, obj, **defaults)

    def response_add(self, request, obj, post_url_continue=None):
        """
        Determines the HttpResponse for the add_view stage. It mostly defers to
        its superclass implementation but is customized because the Product
        model has a slightly different workflow.
        """
        # We should allow further modification of the user just added i.e. the
        # 'Save' button should behave like the 'Save and continue editing'
        # button except in two scenarios:
        # * The user has pressed the 'Save and add another' button
        # * We are adding a user in a popup
        if '_addanother' not in request.POST and IS_POPUP_VAR not in request.POST:
            request.POST['_continue'] = 1
        return super(ProductAdmin, self).response_add(request, obj,
                                                      post_url_continue)


class VariantAdmin(admin.ModelAdmin):

    add_form = VariantCreationForm

    def __init__(self, *args, **kwargs):
        super(VariantAdmin, self).__init__(*args, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults['form'] = PopulatedFormFactory(request, models.Variant,
                self.add_form)
        defaults.update(kwargs)
        return super(VariantAdmin, self).get_form(request, obj, **defaults)


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Variant, VariantAdmin)
