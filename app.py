from flask import Flask, render_template, jsonify, redirect, request, send_from_directory
from lxml import html
from bs4 import BeautifulSoup as bs
from bson.json_util import dumps
from re import sub
from decimal import Decimal

import requests
import json
import pymongo
import pandas as pd
import numpy as np
import csv
import os
import io

import zillow_scrape
import gradient_boosting_model


app = Flask(__name__)


# home page
@app.route("/")
def home():
    return send_from_directory("templates", "index.html")


# build data for the plotly chart from Zillow housing data
@app.route("/zillow")
def get_data():
    city = "kansas-city_rb"
    return zillow_scrape.get_zillow_data(city)




@app.route('/<path:path>')
def send_static_file(path):
    return send_from_directory("", path)



if __name__ == "__main__":
    app.run(debug=True)

  