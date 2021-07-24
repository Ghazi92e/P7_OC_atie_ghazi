# coding=utf-8
import requests
from flask import Flask, request, render_template, jsonify
from api.api import Api
from parsing.parse import Parse

app = Flask(__name__)
api = Api()
parsing = Parse()


@app.route('/')
def index():
    """Initialise the base templates(endpoints)"""
    return render_template('index.html')


@app.route('/ajaxtest', methods=['POST'])
def ajaxtest():
    """Used to display address send by user(AJAX) and the address description"""
    data = request.form['address']
    data_parse = parsing.filterdata(data)
    address = api.geocode(data_parse)
    wikiaddress = api.wikigeocode(data_parse)
    datawiki = api.wikiapi(wikiaddress)
    return jsonify({'output': address, 'wikidata': datawiki})
