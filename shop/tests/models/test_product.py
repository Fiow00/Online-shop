from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from shop.models import Product, Category


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name="Books",
            slug="books",
        )

    def setUp(self):
        self.product = Product.objects.create(
            category=self.category,
            name="Django for Beginners",
            slug="django-for-beginners",
            description="A beginner-friendly Django book.",
            price=Decimal("29.99"),
            available=True,
        )

    def test_product_name(self):
        self.assertEqual(self.product.name, "Django for Beginners")

    def test_product_slug(self):
        self.assertEqual(self.product.slug, "django-for-beginners")

    def test_product_description(self):
        self.assertEqual(
            self.product.description,
            "A beginner-friendly Django book."
        )

    def test_product_price(self):
        self.assertEqual(self.product.price, Decimal("29.99"))

    def test_product_available(self):
        self.assertTrue(self.product.available)

    def test_product_category(self):
        self.assertEqual(self.product.category, self.category)

    def test_product_str(self):
        self.assertEqual(str(self.product), "Django for Beginners")

    def test_product_created_at(self):
        self.assertIsNotNone(self.product.created_at)

    def test_product_updated_at(self):
        self.assertIsNotNone(self.product.updated_at)

    def test_product_verbose_name(self):
        self.assertEqual(Product._meta.verbose_name, "product")

    def test_product_verbose_name_plural(self):
        self.assertEqual(Product._meta.verbose_name_plural, "products")

    def test_product_ordering(self):
        self.assertEqual(Product._meta.ordering, ["name"])

    def test_product_default_available(self):
        product = Product.objects.create(
            category=self.category,
            name="Python Crash Course",
            slug="python-crash-course",
            price=Decimal("19.99"),
        )
        self.assertTrue(product.available)

    def test_product_can_be_updated(self):
        self.product.price = Decimal("39.99")
        self.product.save()

        updated_product = Product.objects.get(pk=self.product.pk)
        self.assertEqual(updated_product.price, Decimal("39.99"))

    def test_get_absolute_url(self):
        self.assertEqual(self.product.get_absolute_url(), reverse("shop:product_detail", args=[self.product.id, self.product.slug]))