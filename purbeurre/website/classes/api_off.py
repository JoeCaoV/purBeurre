"""Module to request the API"""
import requests

class ApiOff:
    """Contains the methods to request the OpenfoodFact Api
    Documentation : https://en.wiki.openfoodfacts.org/API
    """

    def __init__(self):
        self.search_url = 'https://fr-en.openfoodfacts.org/cgi/search.pl'

    def research_products(self, category, quantity):
        """Research and return the first product found
        according to the research terms
        """
        params = {'search_terms' : category, 'json' : 1}
        api_get = requests.get(self.search_url, params=params).json()
        try:
            products = api_get['products']
        except:
            return False
        else:
            result = []
            for count, product in enumerate(products):
                if len(result) < quantity:
                    try:
                        product = {'name': api_get['products'][count]['product_name_fr'],
                                   'url': api_get['products'][count]['url'],
                                   'nutriscore': api_get['products'][count]['nutriments']['nutrition-score-fr'],
                                   'image_url': api_get['products'][count]['image_front_url'],
                                   'categories': api_get['products'][count]['categories']}
                    except IndexError:
                        break
                    except:
                        continue
                    else:
                        result.append(product)
            return result
