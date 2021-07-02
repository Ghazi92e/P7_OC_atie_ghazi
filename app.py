# coding=utf-8
import requests
from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

import stop_words
from stop_words import STOP_WORDS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ghazi:Liban@localhost/todotest'
db = SQLAlchemy(app)


class Task(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)


bots = ['Salut cest papyGrantbot', 'cest le bot']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/testgooglemaps', methods=['GET', 'POST'])
def testgooglemaps():
    if request.method == 'POST':
        filtertext = request.form.get('parsetext')
        filterdata(filtertext)
    else:
        return render_template('testgooglemaps.html')
    return render_template('tesgooglemap.html', filtertext=filtertext)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.name = request.form.get('name')
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('update.html', task=task)


@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/api/get-json', methods=['GET', 'POST'])
def hello():
    req = request.get_data()
    return jsonify({'data': req})


def filterdata(data_user):
    filter_data = []
    for data in data_user.split():
        if data not in STOP_WORDS:
            filter_data.append(data)
    return filter_data


"""
@app.route('/filter', methods=['GET', 'POST'])
def filterdataa():
    filter_data = []
    data_user = "quelle est l'adresse de Paris"
    if request.method == 'POST':
        name = request.form.get('parsetext', '').split()
        if name not in STOP_WORDS:
            filter_data.append(name)
    return jsonify(data=filter_data)
"""

"""
@app.route('/bot', methods=['POST'])
def bot():
    name = request.form['botgeo']
    proc = name
    d = filterdata(proc)
    test = geocode(d)
    print(geocode(d))
    return render_template('bot.html', ok=name, data=test)
"""


def geocode(address):
    data = []
    GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={}/&key='.format(
        address)

    req = requests.get(GOOGLE_MAPS_API_URL)
    d = req.json()
    data.append(d)
    if address:
        for datageo in data:
            return datageo["results"][0]["formatted_address"]


def wikigeocode(address):
    data = []
    GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={}/&key='.format(
        address)

    req = requests.get(GOOGLE_MAPS_API_URL)
    d = req.json()
    data.append(d)
    if address:
        for datageo in data:
            return datageo['results'][0]['address_components'][0]['long_name']


@app.route('/ajaxtest', methods=['POST'])
def ajaxtest():
    global address
    global wikipageid
    data = request.form['address']
    data_parse = filterdata(data)
    address = geocode(data_parse)
    wikiaddress = wikigeocode(data_parse)
    datawiki = []
    MEDIA_WIKI_API = "http://fr.wikipedia.org/w/api.php"
    params = {
        "format": "json",
        "action": "query",
        "prop": "extracts",
        "explaintext": "",
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


@app.route('/wikimedia')
def wikimedia():
    global wikipageid
    datawiki = []
    MEDIA_WIKI_API = "http://fr.wikipedia.org/w/api.php"
    params = {
        "format": "json",
        "action": "query",
        "prop": "extracts",
        "explaintext": "",
        "titles": "cité Paradis"
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
        return titleinfo
