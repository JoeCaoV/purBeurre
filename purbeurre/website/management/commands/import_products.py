from django.core.management.base import BaseCommand, CommandError
from website.classes.api_off import ApiOff
from website.config import CATEGORIES
from website.models import Category, Product

class Command(BaseCommand):
    help = 'Populate our Product Database with data from OpenFoodFact'

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Quantity of product you want to import for each category')

    def handle(self, *args, **kwargs):
        quantity = kwargs['quantity']
        api_off = ApiOff()
        for category in CATEGORIES:
            try:  
                model_category = Category.objects.get(name=category)
            except:
                model_category = Category(name=category)
                model_category.save()

            products = api_off.research_products(category, quantity)
            for product in products:
                try:
                    model = Product(**product, category=model_category)
                    model.save()
                except:
                    continue
