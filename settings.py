import os
from os import environ

API_GOOGLEMAPS_KEY = environ.get('API_GOOGLEMAPS_KEY')

is_prod = os.environ.get('API_GOOGLEMAPS_KEY', None)
if is_prod:
    API_GOOGLEMAPS_KEY = environ.get('API_GOOGLEMAPS_KEY')
