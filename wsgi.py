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
    return mydb2.get_car_images()

if __name__ == "__main__":
    application.run()