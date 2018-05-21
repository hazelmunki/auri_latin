# -*- coding: utf-8 -*-
import flask
from flask import request, jsonify, json, render_template
import re

app = flask.Flask(__name__)
app.config["DEBUG"] = True

d = json.load(open("dict.json"))


@app.route("/")
def hello():
    return "Test!"

@app.route("/search/<eng_id>", methods=["GET"])
def search_eng(eng_id):
    res = []
    for i in d:
        if eng_id in i["definition"]:
            pp = [i["principalParts"] for i["principalParts"] in d]
            defi = i["definition"]
            pos = i["partOfSpeech"]
            res += pp, defi, pos
    return render_template("index.html", res=res)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
