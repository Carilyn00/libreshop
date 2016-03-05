import logging
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.test import TestCase
from inventory.models import Inventory, Attribute, Attribute_Value
from ...models import Product, Variant, Component

# Initialize logger.
logger = logging.getLogger(__name__)

# Create your tests here.
class ProductModelTest(TestCase):

    def test_model_has_sku_field(self):
        '''
        Test that Product.sku is present.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        sku = None
        try:
            sku = product._meta.get_field('sku')
        except:
            pass
        self.assertIsNotNone(sku)


    def test_model_sku_field_is_unique(self):
        '''
        Test that Product.sku is unique.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        sku = None
        try:
            sku = product._meta.get_field('sku')
        except:
            pass
        unique = getattr(sku, 'unique', None)
        self.assertTrue(unique)


    def test_sku_field_must_be_unique_regardless_of_character_case(self):
        '''
        Test that Product.sku must be unique regardless of character case.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        func = Product.objects.create
        self.assertRaises(ValidationError, func, sku='Foo', name='bar')


    def test_model_sku_field_is_required(self):
        '''
        Test that Product.sku is required.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        sku = None
        try:
            sku = product._meta.get_field('sku')
        except:
            pass
        nullable = getattr(sku, 'null', None)
        self.assertFalse(nullable)


    def test_model_sku_field_cannot_be_blank(self):
        '''
        Test that Product.sku does not allow blank values in forms.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        sku = None
        try:
            sku = product._meta.get_field('sku')
        except:
            pass
        blank = getattr(sku, 'blank', None)
        self.assertFalse(blank)


    def test_model_sku_field_has_max_length(self):
        '''
        Test that Product.sku max length is 8.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        sku = None
        try:
            sku = product._meta.get_field('sku')
        except:
            pass
        max_length = getattr(sku, 'max_length', None)
        self.assertEqual(max_length, 8)


    def test_model_sku_field_has_verbose_name(self):
        '''
        Test that Product.sku's verbose name is 'SKU'.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        sku = None
        try:
            sku = product._meta.get_field('sku')
        except:
            pass
        verbose_name = getattr(sku, 'verbose_name', None)
        self.assertEqual(verbose_name, 'SKU')


    def test_model_sku_field_has_verbose_name_plural(self):
        '''
        Test that Product.sku's plural verbose name is 'SKUs'.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        sku = None
        try:
            sku = product._meta.get_field('sku')
        except:
            pass
        verbose_name_plural = getattr(sku, 'verbose_name_plural', None)
        self.assertEqual(verbose_name_plural, 'SKUs')


    def test_model_has_name_field(self):
        '''
        Test that Product.name is present.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        name = None
        try:
            name = product._meta.get_field('name')
        except:
            pass
        self.assertIsNotNone(name)


    def test_model_name_field_is_unique(self):
        '''
        Test that Product.name is unique.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        name = None
        try:
            name = product._meta.get_field('name')
        except:
            pass
        unique = getattr(name, 'unique', None)
        self.assertTrue(unique)


    def test_name_field_must_be_unique_regardless_of_character_case(self):
        '''
        Test that Product.name must be unique regardless of character case.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        func = Product.objects.create
        self.assertRaises(ValidationError, func, sku='bar', name='Foo')


    def test_model_name_field_is_required(self):
        '''
        Test that Product.name is required.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        name = None
        try:
            name = product._meta.get_field('name')
        except:
            pass
        nullable = getattr(name, 'null', None)
        self.assertFalse(nullable)


    def test_model_name_field_cannot_be_blank(self):
        '''
        Test that Product.name does not allow blank values in forms.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        name = None
        try:
            name = product._meta.get_field('name')
        except:
            pass
        blank = getattr(name, 'blank', None)
        self.assertFalse(blank)


    def test_model_name_field_has_max_length(self):
        '''
        Test that Product.name max length is 64.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        name = None
        try:
            name = product._meta.get_field('name')
        except:
            pass
        max_length = getattr(name, 'max_length', None)
        self.assertEqual(max_length, 64)


    def test_model_has_attributes_property(self):
        '''
        Test that Product.attributes is present.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        attributes = getattr(product, 'attributes', None)
        self.assertIsNotNone(attributes)


    def test_attributes_property_inherits_child_variant_attributes(self):
        '''
        Test that Product.attributes contains attributes from its child Variant
        object(s).
        '''
        product = Product.objects.create(sku='foo', name='foo')
        variant = Variant.objects.create(product=product, name='bar')
        inventory = Inventory.objects.create(name='baz')
        attribute = Attribute.objects.create(name='foo')
        attribute_value = Attribute_Value.objects.create(attribute=attribute,
            inventory=inventory, value='bar')
        component = Component.objects.create(variant=variant,
            inventory=inventory, quantity=Decimal(1.00))
        attributes = getattr(product, 'attributes', None)
        self.assertIn('foo', attributes)


    def test_attributes_property_inherits_child_variant_attributes_as_list(self):
        '''
        Test that Product.attributes contains a list of attribute values, when
        child Variants contain matching attributes.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        variant1 = Variant.objects.create(product=product, name='bar')
        variant2 = Variant.objects.create(product=product, name='baz')
        attribute = Attribute.objects.create(name='foo')
        inventory = Inventory.objects.create(name='baz')
        attribute_value = Attribute_Value.objects.create(attribute=attribute,
            inventory=inventory, value='bar')
        component1 = Component.objects.create(variant=variant1,
            inventory=inventory, quantity=Decimal(1.00))
        componen2 = Component.objects.create(variant=variant2,
            inventory=inventory, quantity=Decimal(1.00))
        attributes = getattr(product, 'attributes', None)
        self.assertEqual({'foo': ['bar']}, attributes)


    def test_saving_to_and_retrieving_products_from_the_database(self):
        '''
        Test that a Product can be successfuly saved to the database.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        num_products = Product.objects.all().count()
        self.assertEqual(num_products, 1)


    def test_creating_exactly_one_variant_alongside_product(self):
        '''
        Test that a Variant is created on the `many` side of the mandatory
        1-to-Many relationship between Products and Variants.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        num_variants = Variant.objects.all().count()
        self.assertEqual(num_variants, 1)


    def test_single_variant_has_same_name_as_parent_product_at_creation(self):
        '''
        Test that a single child Variant inherits the name of its parent
        Product.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        variants = Variant.objects.filter(product=product)
        variant = variants[0] if variants else None
        self.assertEqual(product.name, variant.name)


    def test_single_variant_has_same_name_as_parent_product_at_variant_update(self):
        '''
        Test that a single child Variant cannot change its name from the name
        inherited from its parent Product.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        variants = Variant.objects.filter(product=product)
        variant = variants[0] if variants else None
        variant.name = 'bar'
        variant.save()
        self.assertEqual(product.name, variant.name)


    def test_single_variant_has_same_name_as_parent_product_at_sibling_deletion(self):
        '''
        Test that a child Variant with siblings takes the name of its parent
        Product when it becomes an only child.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        variant1 = Variant.objects.filter(product=product)[0]
        variant2 = Variant.objects.create(name='baz', product=product)
        variant1.name = 'bar'
        variant1.save()
        variant1.refresh_from_db()
        variant2.delete()
        variant1.refresh_from_db()
        self.assertEqual(variant1.name, 'foo')


    def test_single_variant_has_same_name_as_parent_product_at_product_update(self):
        '''
        Test that a child Variant takes the name of its parent Product when the
        parent changes its name.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        variants = Variant.objects.filter(product=product)
        variant = variants[0] if variants else None
        product.name = 'bar'
        product.save()
        variant.refresh_from_db()
        self.assertEqual(product.name, variant.name)


    def test_sibling_variant_can_have_different_name(self):
        '''
        Test that a sibling Variant can change its name.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        variant1 = Variant.objects.filter(product=product)[0]
        variant2 = Variant.objects.create(name='baz', product=product)
        self.assertNotEqual(variant1.name, variant2.name)


    def test_original_variant_can_be_renamed_when_sibling_present(self):
        '''
        Test that the first child Variant can change its name, when siblings
        are present.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        variant1 = Variant.objects.filter(product=product)[0]
        variant2 = Variant.objects.create(name='baz', product=product)
        variant1.name = 'bar'
        variant1.save()
        variant1.refresh_from_db()
        self.assertEqual(variant1.name, 'bar')


    def test_original_variant_is_not_renamed_at_product_update_when_sibling_present(self):
        '''
        Test that the first child Variant does not inherit its parent's name
        when a sibling is present.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        variant1 = Variant.objects.filter(product=product)[0]
        variant2 = Variant.objects.create(name='baz', product=product)
        product.name = 'bar'
        product.save()
        product.refresh_from_db()
        self.assertEqual(variant1.name, 'foo')


    def test_sibling_variant_is_not_renamed_at_product_update_when_sibling_present(self):
        '''
        Test that any subsequent child Variants do not inherit their parent's
        name when a sibling is present.
        '''
        product = Product.objects.create(sku='foo', name='foo')
        variant1 = Variant.objects.filter(product=product)[0]
        variant2 = Variant.objects.create(name='baz', product=product)
        product.name = 'bar'
        product.save()
        product.refresh_from_db()
        self.assertEqual(variant2.name, 'baz')
