import os
import json
from flask import Flask
from db2client import db2Access

mydb2 = db2Access()

application = Flask(__name__)

@application.route("/")
def hello():
    return "OpenShift Hello World 4!"

@application.route("/cars")
def cars():
    return mydb2.get_categorized_images('C')

@application.route("/persons")
def persons():
    return mydb2.get_categorized_images('P')

if __name__ == "__main__":
    application.run()