import os
import json
from flask import Flask
from db2client import db2Access
from flask import make_response
from requests import get

mydb2 = db2Access()

application = Flask(__name__)

#@application.route("/")
#def hello():
#    return "OpenShift Hello World 4!"

@application.route("/cars")
def cars():
    r = make_response(mydb2.get_categorized_images('C'))
    r.headers.set('Access-Control-Allow-Origin', 'appdomain.cloud')
    return r

@application.route("/persons")
def persons():
    r = make_response(mydb2.get_categorized_images('P'))
    r.headers.set('Access-Control-Allow-Origin', 'appdomain.cloud')
    return r

SITE_NAME="https://s3.eu-de.cloud-object-storage.appdomain.cloud/osw-bucket-glwiosgnsciuvwlto/"

@application.route('/', defaults={'path': 'myjavascript.html'})
@application.route('/<path:path>')
def proxy(path):
  return get(f'{SITE_NAME}{path}').content

if __name__ == "__main__":
    application.run()