# coding=utf-8
from flask import Flask, request, render_template, jsonify
from api.api import Api
from parsing.parse import Parse

app = Flask(__name__)


@app.route('/')
def index():
    """Initialise the base templates(endpoints)"""
    return render_template('index.html')


@app.route('/ajaxtest', methods=['POST'])
def ajaxtest():
    """Used to display address send by user(AJAX)
    and the address description"""
    data = request.form['address']
    parsing = Parse()
    data_parse = parsing.filterdata(data)
    api = Api()
    address = api.geocode(data_parse)
    wikiaddress = api.wikigeocode(data_parse)
    datawiki = api.wikiapi(wikiaddress)
    return jsonify({'output': address, 'wikidata': datawiki})
