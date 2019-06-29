CATEGORIES = [
    'pizzas', 'Pâtes à tartiner', 'salades', 'glaces', 'moutardes',
    'biscuits', 'pains', 'cafés', 'brownies', 'saucisses',
    'mueslis', 'smoothies', 'boissons énergisantes', 'Sandwichs', 'boissons au thé'
    ]

"""This long dict contains 3 article for 8 differents categories
each 3th product got a missing attribut, to check if the program
notice it
"""
PRODUCTS_MOCK = [
            #pizzas    
            [
                {
                    'name': 'name',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name2',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name3',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #Pâtes à tartiner
            [
                {
                    'name': 'name4',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name5',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name6',
                    'image_url': 'image_url',
                    'nutrigrade': 'b',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #salades
            [
                {
                    'name': 'name7',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name8',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name9',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore': 10,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #glaces
            [
                {
                    'name': 'name10',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name11',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name12',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #moutardes
            [
                {
                    'name': 'name13',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name14',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name15',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #biscuits
            [
                {
                    'name': 'name16',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name17',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name18',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 40.2,
                    'url': 'url.com'
                },               
            ],
            #pains
            [
                {
                    'name': 'name19',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name20',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name21',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 40.2,
                    'calories': 50,
                },               
            ],
            #cafés
            [
                {
                    'name': 'name22',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name23',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name23bis',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 40.2,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #brownies
            [
                {
                    'name': 'name24',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name25',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name26',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 40.2,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #saucisses
            [
                {
                    'name': 'name27',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name28',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name29',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 40.2,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #mueslis
            [
                {
                    'name': 'name30',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name31',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name32',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 40.2,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #smoothies
            [
                {
                    'name': 'name33',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name34',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name35',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 40.2,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #boissons énergisantes
            [
                {
                    'name': 'name36',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name37',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name38',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 40.2,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #Sandwichs
            [
                {
                    'name': 'name39',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name40',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name41',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 40.2,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
            #boissons au thé
            [
                {
                    'name': 'name42',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':25,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name43',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 30.9,
                    'calories': 50,
                    'url': 'url.com'
                },
                {
                    'name': 'name44',
                    'image_url': 'image_url',
                    'nutrigrade':'e',
                    'nutriscore':15,
                    'salt': 0.1,
                    'sugar': 56.3,
                    'fat': 40.2,
                    'calories': 50,
                    'url': 'url.com'
                },               
            ],
        ]
