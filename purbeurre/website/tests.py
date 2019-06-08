from django.test import TestCase
from mock import patch
from .classes.api_off import ApiOff
# Create your tests here.

class ApiOpenFood(TestCase):
    """Contain the test for the OpenFoodFact Api"""

    def setUp(self):
        self.api = ApiOff()

    @patch('requests.get')
    def test_working_request(self, mock_api):
        """Testing a wanted result"""
        api_result = {'products' :
                      [
                          {
                            'product_name_fr': 'name',
                            'url': 'url',
                            'image_front_url': 'image_url',
                            'nutriments':{
                                'nutrition-score-fr':25
                            },
                            'categories': 'Pate à pain'
                          }
                      ]
                     }
        mock_api.return_value.json.return_value = api_result
        response = {'name': 'name',
                    'url': 'url',
                    'nutriscore': 25,
                    'image_url': 'image_url',
                    'categories': 'Pate à pain'}
        self.assertEqual(response, self.api.research_product('test'))

    @patch('requests.get')
    def test_failing_request(self, mock_api):
        """Testing a failing result"""
        mock_api.return_value.json.return_value = 'Nope'
        self.assertFalse(self.api.research_product('test'))
        
