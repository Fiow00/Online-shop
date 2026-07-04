from django.test import TestCase
from django.db import IntegrityError

from shop.models import Category

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name="Books",
            slug="books"
        )

    def setUp(self):
        self.category = Category.objects.get(pk=self.category.pk)

    def test_category_name(self):
        self.assertEqual(self.category.name, "Books")

    def test_category_slug(self):
        self.assertEqual(self.category.slug, "books")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Books")

    def test_category_verbose_name(self):
        self.assertEqual(Category._meta.verbose_name, "category")

    def test_category_verbose_name_plural(self):
        self.assertEqual(Category._meta.verbose_name_plural, "categories")

    def test_category_ordering(self):
        self.assertEqual(Category._meta.ordering, ["name"])

    def test_category_slug_is_unique(self):
        with self.assertRaises(IntegrityError):
            Category.objects.create(
                name="Programming",
                slug="books",
            )