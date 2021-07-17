# coding=utf-8
import requests
from flask import Flask, request, render_template, jsonify
from api.api import Api
from stop_words import STOP_WORDS

app = Flask(__name__)
api = Api()


@app.route('/')
def index():
    return render_template('index.html')


def filterdata(data_user):
    filter_data = []
    for data in data_user.split():
        if data not in STOP_WORDS:
            filter_data.append(data)
    return filter_data


@app.route('/ajaxtest', methods=['POST'])
def ajaxtest():
    wikipageid = None
    data = request.form['address']
    data_parse = filterdata(data)
    address = api.geocode(data_parse)
    wikiaddress = api.wikigeocode(data_parse)
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
