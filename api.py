# coding: utf-8
from __future__ import unicode_literals
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json 

app = Flask(__name__)
CORS(app)


# Route : hello
@app.route("/hello")
def hello():
  return "hello"

if __name__ == '__main__' :
  app.run(debug=True)