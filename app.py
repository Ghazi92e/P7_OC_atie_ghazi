import json
import urllib.request

import requests
from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

import stop_words
from parsedata import filterdata
from stop_words import STOP_WORDS

app = Flask(__name__)  # Crée une instance de la classe Flask, c'est notre application
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ghazi:Liban@localhost/todotest'  # Nom de la BDD
db = SQLAlchemy(app)  # Lie l'app à SQLAlchemy


class Task(db.Model):  # Modèle
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)


bots = ['Salut cest papyGrantbot', 'cest le bot']


@app.route('/')
def index():
    return render_template('index.html')

    """
    name = request.form['parsetext']  # Récupérer les données envoyées par le form
    proc = name
    d = filterdata(proc)
    test = geocode(d)
    print(geocode(d))
    return render_template('index.html', ok=name, data=test)
    if name:
    filterdata(name)
    task = Task(name=name)  # Créer la tache dans la BDD avec le modèle Task
    db.session.add(task)  # Ajout de notre objet à la session
    db.session.commit()  # Enregistrer la tache dans la BDD
    data = Task.query.all()
    return render_template('index.html', data=data)
"""


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


@app.route('/filter', methods=['GET', 'POST'])
def filterdataa():
    filter_data = []
    data_user = "quelle est l'adresse de Paris"
    if request.method == 'POST':
        name = request.form.get('parsetext', '').split()
        if name not in STOP_WORDS:
            filter_data.append(name)
    return jsonify(data=filter_data)


@app.route('/bot', methods=['POST'])
def bot():
    name = request.form['botgeo']  # Récupérer les données envoyées par le form
    proc = name
    d = filterdata(proc)
    test = geocode(d)
    print(geocode(d))
    return render_template('bot.html', ok=name, data=test)


def geocode(address):
    data = []
    GOOGLE_MAPS_API_URL = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key='

    req = requests.get(GOOGLE_MAPS_API_URL)
    d = req.json()
    data.append(d)
    for datageo in data:
        return datageo["results"][0]["formatted_address"]


@app.route('/ajaxtest', methods=['POST'])
def ajaxtest():
    data = request.form['address']
    output = data
    d = filterdata(output)
    test = geocode(d)
    print(test)
    return jsonify({'output':test})
