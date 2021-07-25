import json

import requests

from api.api import Api
from parsing.parse import Parse

api = Api()
pars = Parse()


class MockResponse:
    """Use Mock for API test"""
    def __init__(self, filepath):
        """Get filepath json file"""
        self.filepath = filepath

    def json(self):
        """Open API json file"""
        with open(self.filepath) as json_file:
            data = json.load(json_file)
            return data


def test_api(monkeypatch):
    """Test API Google Maps and Media Wiki with fake request (monkeypatch)"""

    def mock_get_googlamaps(*args, **kwargs):
        """Get the API Google Maps JSON structure"""
        return MockResponse('apigooglemaps.json')

    def mock_get_mediawiki(*args, **kwargs):
        """Get the API Media Wiki JSON structure"""
        return MockResponse('apimediawiki.json')

    """Test API Google Maps for Media Wiki"""
    monkeypatch.setattr(requests, "get", mock_get_googlamaps)
    res = api.wikigeocode("https://fakeurl")
    assert res == "Quai de la Charente"
    """Test API Google Maps"""
    monkeypatch.setattr(requests, "get", mock_get_googlamaps)
    res = api.geocode("https://maps.googleapis.com/maps/fake")
    assert res == "10 Quai de la Charente, 75019 Paris, France"
    """Test API Media Wiki"""
    monkeypatch.setattr(requests, "get", mock_get_mediawiki)
    res = api.wikiapi("https://fakeurlmediawiki")
    assert res == "Le quai de la Charente est un quai situé " \
                  "le long du canal Saint-Denis, à Paris, " \
                  "dans le 19e arrondissement."


def test_filterdata():
    """Test filterdata method"""
    assert pars.filterdata("adresse de paris") == ["paris"]
    assert pars.filterdata("Quelle est l'adresse de OpenClassrooms ?") \
           == ["OpenClassrooms"]
    assert pars.filterdata("Salut GrandPy ! Est-ce que tu connais "
                           "l'adresse de OpenClassrooms ?") \
           == ["OpenClassrooms"]
    assert pars.filterdata("Quelle est l'adresse du futuroscope ?") == ["futuroscope"]
