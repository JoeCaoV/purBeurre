from django.core.management.base import BaseCommand, CommandError
from website.models import Category, Product

class Commad(BaseCommand):
    help = 'Populate our Product Database with data from OpenFoodFact'

    