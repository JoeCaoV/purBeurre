"""Module to request the API"""

class ApiOff:
    """Contains the methods to request the OpenfoodFact Api
    Documentation : https://en.wiki.openfoodfacts.org/API
    """

    def __init__(self):
        self.search_url = 'https://fr-en.openfoodfacts.org/cgi/search.pl'

    def research_product(self, terms):
        params = {'search_terms' : terms, 'search_simple' : 1, 'json' : 1}
        api_get = requests.get(self.search_url, params=params).json()
        product = { 
            'name' : products[0]['product_name_fr'],
            'url' : [products][0]['url'],
            'nutriscore' : [products][0]['nutriments']['nutrition-score-fr'],
            'image_url' : [products][0]['image_front_url'],
        }
        return product
