from flask import Flask, render_template, request, jsonify
import requests


def append_coords(to, new):
    if new not in to:
        to.append(new)
    return to


app = Flask(__name__)
app.config["SECRET_KEY"] = "maper.io geo"


@app.route("/", methods=["GET", "POST"])
def index():
    global coords
    if request.method == "GET":
        return render_template("index.html")
    else:
        a = request.form
        coords = append_coords(coords, a["lon"] + "," + a["lat"])
        params = {
            "ll": ",".join([a["lon"], a["lat"]]),
            "l": "map",
            "pt": ",".join([a["lon"], a["lat"], "ya_ru"]),
            "pl": ",".join(coords),
        }
        return requests.get("https://static-maps.yandex.ru/1.x/", params=params).url


coords = []
