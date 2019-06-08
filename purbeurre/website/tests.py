from django.test import TestCase
from .classes import api_off
# Create your tests here.

class ApiOpenFood(TestCase):
    def setUp(self):
        self.api = ApiOff()

    def test_api(self):
        product = self.api.research_product('nutella')
        print(product)
