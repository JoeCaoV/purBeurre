from django.core.management import call_command
from django.test import TransactionTestCase
from website.config import CATEGORIES
from website.models import Category, Product

class Populate_database(TransactionTestCase):
    """contain the test of the command 'import_products'"""
    def test_import_product(self):
        """Try the command and print the list of insered products"""
        result = call_command('import_products', '50')
        for category in CATEGORIES:
            category_object = Category.objects.get(name=category)
            products = Product.objects.filter(category=category_object)
            print(len(products), 'produits importés dans la catégorie', category)
