import logging
from decimal import Decimal
from django.db import models
from django.db import transaction
from model_utils.models import TimeStampedModel
from jsonfield import JSONField
from inventory.models import Inventory

# Initialize logger.
logger = logging.getLogger(__name__)

# Create your models here.
class ProductManager(models.Manager):

    def create(self, *args, **kwargs):
        product = None
        with transaction.atomic():
            product = super(ProductManager, self).create(*args, **kwargs)
            variant = Variant.objects.create(product=product,
                name=product.name)

        return product


class Product(TimeStampedModel):

    sku = models.CharField(max_length=8,
                           unique=True,
                           null=False)
    name = models.CharField(max_length=64,
                            unique=True,
                            null=False,
                            blank=False)

    objects = ProductManager()

    def save(self, *args, **kwargs):
        product = None
        with transaction.atomic():

            product = super(Product, self).save(*args, **kwargs)
            variants = Variant.objects.filter(product=self)

            if not variants:
                variant = Variant.objects.create(product=self,
                    name=self.name)

            if variants.count() == 1 and self.name != variants[0].name:
                variant = variants[0]
                variant.name = self.name
                variant.save(*args, **kwargs)

        return product

    def __str__(self):
        return self.name


class VariantManager(models.Manager):

    def create(self, *args, **kwargs):
        variant = None
        with transaction.atomic():
            variant = super(VariantManager, self).create(*args, **kwargs)
            component = Component.objects.filter(variant=variant)
            if not component:
                component = Component.objects.create(variant=variant)

        return variant


class Variant(TimeStampedModel):

    product = models.ForeignKey(Product)
    name = models.CharField(max_length=64,
                            null=True,
                            blank=True)
    sub_sku = models.CharField(max_length=8,
                               null=True,
                               blank=True)
    price = models.DecimalField(max_digits=8,
                                decimal_places=2,
                                null=False,
                                default=Decimal('0.00'))

    objects = VariantManager()

    def save(self, *args, **kwargs):
        variant = None
        with transaction.atomic():
            if (self.product.name != self.name and self.product.variant_set.
                count() == 1):
                self.name = self.product.name

            variant = super(Variant, self).save(*args, **kwargs)

            components = Component.objects.filter(variant=self)

            if not components:
                component = Component.objects.create(variant=self)

        return variant

    def delete(self, *args, **kwargs):
        super(Variant, self).delete(*args, **kwargs)

        product = Product.objects.get(id=self.product_id)
        variants = Variant.objects.filter(product=self.product)

        if product and not variants:
            variant = Variant.objects.create(product=self.product)

        if (self.product.variant_set.count() == 1):
            variant = self.product.variant_set.first()
            variant.name = self.product.name
            variant.save(*args, **kwargs)

    def __str__(self):
        return self.name or 'Variant(%s) of Product: %s' % (self.id, self.product.sku)


class Component(TimeStampedModel):

    variant = models.ForeignKey(Variant)
    inventory = models.ForeignKey(Inventory,
                                  blank=True,
                                  null=True)
    quantity = models.DecimalField(max_digits=8,
                                   decimal_places=2,
                                   null=False,
                                   default=Decimal('0.00'))

    def delete(self, *args, **kwargs):
        super(Component, self).delete(*args, **kwargs)

        variant = Variant.objects.get(id=self.variant_id)
        components = Component.objects.filter(variant=self.variant)

        if variant and not components:
            component = Component.objects.create(variant=self.variant)

    def __str__(self):
        return 'Component of %s' % self.variant.name
