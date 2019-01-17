from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """
    Define tests that will run again the Product models
    """

    def test_str(self):
        test_name = Product(name=" A Product")
        self.assertEqual(str(test_name), "A Product")