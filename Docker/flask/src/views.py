import random
import requests
from flask import render_template

from src import src

@src.route("/")
def index():
    return render_template("index.html")


@src.route("/conseil")
def conseil():
    url = 'https://api.adviceslip.com/advice'
    try:
        resp = requests.get(url)
        data = resp.json()
        advice = data['slip']['advice']
        print(advice)

        return render_template("conseil.html", conseil=advice)
    except ValueError:
        return render_template("error.html")