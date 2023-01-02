import random
import requests
from flask import render_template

from app import app

@app.route("/")
def index():
    return render_template("index.html", codes=CODES)


@app.route("/conseil")
def conseil():
    url = 'https://api.adviceslip.com/advice'
    try:
        resp = requests.get(url=url)
        data = resp.json()

        return render_template("conseil.html", conseil=data.slip.advice)
    except ValueError:
        return render_template("unknown.html", codes=CODES, code=code)