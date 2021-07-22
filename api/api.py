import requests
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('settings.py')


class Api:
    def geocode(self, address_maps):
        """Request API Google Maps and return an address"""
        data = []
        GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={}/&region=FR&key={}'.format(
            address_maps, app.config.get("API_GOOGLEMAPS_KEY"))

        req = requests.get(GOOGLE_MAPS_API_URL)
        d = req.json()
        data.append(d)
        for datageo in data:
            return datageo["results"][0]["formatted_address"]

    def wikigeocode(self, address_wiki):
        """Request API Google Maps and return the name of the place address for API Media Wiki"""
        data = []
        GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={}/&region=FR&key={}'.format(
            address_wiki, app.config.get("API_GOOGLEMAPS_KEY"))

        req = requests.get(GOOGLE_MAPS_API_URL)
        d = req.json()
        data.append(d)
        if address_wiki:
            for datageo in data:
                testdata = datageo['results'][0]['address_components'][1]['long_name']
                return testdata
