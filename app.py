# coding=utf-8
import requests
from flask import Flask, request, render_template, jsonify
from stop_words import STOP_WORDS

app = Flask(__name__)
app.config.from_pyfile('settings.py')


@app.route('/')
def index():
    return render_template('index.html')


def filterdata(data_user):
    filter_data = []
    for data in data_user.split():
        if data not in STOP_WORDS:
            filter_data.append(data)
    return filter_data


def geocode(address_maps):
    data = []
    GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={}/&region=FR&key={}'.format(
        address_maps, app.config.get("API_GOOGLEMAPS_KEY"))

    req = requests.get(GOOGLE_MAPS_API_URL)
    d = req.json()
    data.append(d)
    for datageo in data:
        return datageo["results"][0]["formatted_address"]


def wikigeocode(address_wiki):
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


@app.route('/ajaxtest', methods=['POST'])
def ajaxtest():
    wikipageid = None
    data = request.form['address']
    data_parse = filterdata(data)
    address = geocode(data_parse)
    wikiaddress = wikigeocode(data_parse)
    print(wikiaddress)
    datawiki = []
    MEDIA_WIKI_API = "http://fr.wikipedia.org/w/api.php"
    params = {
        "format": "json",
        "action": "query",
        "prop": "extracts",
        "explaintext": "",
        "exintro": "",
        "titles": f'{wikiaddress}'
    }
    data = requests.get(MEDIA_WIKI_API, params=params)
    d = data.json()
    datawiki.append(d)
    for dw in datawiki:
        idpage = dw['query']['pages']
        for page_id in idpage:
            wikipageid = page_id
    for infodata in datawiki:
        titleinfo = infodata['query']['pages'][wikipageid]['extract']
        return jsonify({'output': address, 'wikidata': titleinfo})

