import requests
import app
from api.api import Api

api = Api()


class MockResponse:
    @staticmethod
    def json():
        return {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "10",
                            "short_name": "10",
                            "types": [
                                "street_number"
                            ]
                        },
                        {
                            "long_name": "Quai de la Charente",
                            "short_name": "Quai de la Charente",
                            "types": [
                                "route"
                            ]
                        },
                    ],
                    "formatted_address": "10 Quai de la Charente, 75019 Paris, France",
                },
            ],
        }


def test_api(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    res = api.wikigeocode("https://fakeurl")
    assert res == "Quai de la Charente"

    monkeypatch.setattr(requests, "get", mock_get)
    res = api.geocode("https://maps.googleapis.com/maps")
    assert res == "10 Quai de la Charente, 75019 Paris, France"


def test_filterdata():
    assert app.filterdata("adresse de paris") == ["paris"]
    assert app.filterdata("Quelle est l'adresse de OpenClassrooms ?") == ["OpenClassrooms"]
    assert app.filterdata("Salut GrandPy ! Est-ce que tu connais l'adresse de OpenClassrooms ?") == ["OpenClassrooms"]
