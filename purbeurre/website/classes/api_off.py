"""Module to request the API"""
import requests

class ApiOff:
    """Contains the methods to request the OpenfoodFact Api
    Documentation : https://en.wiki.openfoodfacts.org/API
    """

    def __init__(self):
        self.search_url = 'https://fr-en.openfoodfacts.org/cgi/search.pl'

    def research_product(self, terms):
        """Research and return the first product found
        according to the research terms
        """
        params = {'search_terms' : terms, 'search_simple' : 1, 'json' : 1}
        api_get = requests.get(self.search_url, params=params).json()
        try:
            product = {'name': api_get['products'][0]['product_name_fr'],
                       'url': api_get['products'][0]['url'],
                       'nutriscore': api_get['products'][0]['nutriments']['nutrition-score-fr'],
                       'image_url': api_get['products'][0]['image_front_url'],
                       'categories': api_get['products'][0]['categories']}
        except:
            return False
        return product

    def research_alternative(self, terms, nutriscore):
        """Research a list of products found according to the research terms
        only return product with a better (smaller) nutriscore  
        """
        pass

