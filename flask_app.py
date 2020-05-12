from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)
app.config["SECRET_KEY"] = "maper.io geo"





@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        a = request.form
        params = {'ll': ','.join([a['lon'], a['lat']]), 'l': 'map', 'pt': ','.join([a['lon'], a['lat'], 'ya_ru'])}
        return requests.get('https://static-maps.yandex.ru/1.x/', params=params).url


