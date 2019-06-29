from django.core.management import call_command
from django.test import TransactionTestCase
from mock import patch
from website.config import CATEGORIES, PRODUCTS_MOCK
from website.models import Category, Product

class PopulateDatabase(TransactionTestCase):
    """contain the test of the command 'import_products'"""

    @patch('website.classes.api_off.ApiOff.research_products', 
           side_effect=PRODUCTS_MOCK)
    def test_import_product(self, mock_api):
        """Try the command and print the list of insered products"""
        call_command('import_products', '4')
        for category in CATEGORIES:
            category_object = Category.objects.get(name=category)
            products = Product.objects.filter(category=category_object)
            self.assertEqual(len(products),3)
            print(len(products), 'produits importés dans la catégorie', category)