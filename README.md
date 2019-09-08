# Purbeurre

Voici le code source du site : 'https://murmuring-falls-38065.herokuapp.com/'

Ce site permet de chercher des aliments, et de trouver des substituts meilleurs et les enregistrer.

### Tester en local : 

Cloner ce repository et créer un fichier secret.py dans purbeurre/purbeurre/ contenant une votre clé secrète dans une variable SECRET_KEY, et vos paramètres de Base de données dans DATABASES_INFO.
Installer les modules, faites les migrations, puis la CLI $ Python purbeurre/manage.py import_products QUANTITY

-- remplacer QUANTITY par un INT de la quantité souhaité de produits à importer par catégories.

Enfin, $ Python purbeurre/manage.py runserver pour lancer le site en local


### Tests unitaire : 

L'application Website, contient un dossier Tests/ contenant les différents tests de ce projets. Pour les 
executer $ Python purbeurre/manage.py test website
