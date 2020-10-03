import os
import json
from flask import Flask
from flask import make_response
from flask import request
from requests import get

application = Flask(__name__)

temperature1 = 0
temperature2 = 0
temperature3 = 0
temperature4 = 0

@application.route("/")
def hello():
    result = "Hello World on Openshift, here is another update!<br>"
    result = result + "Temperature 1:"+str(temperature1)+ " °C<br>"
    result = result + "Temperature 2:"+str(temperature2)+ " °C<br>"
    result = result + "Temperature 3:"+str(temperature3)+ " °C<br>"
    result = result + "Temperature 4:"+str(temperature4)+ " °C<br>" 
    return result

@application.route("/push/", methods=['POST'])
def push():
    temperature1 = float(request.form.get('temperature1'))
    return "got it..."

@application.route("/persons")
def persons():
    r.headers.set('Access-Control-Allow-Origin', 'appdomain.cloud')
    return r

SITE_NAME="https://s3.eu-de.cloud-object-storage.appdomain.cloud/osw-bucket-glwiosgnsciuvwlto/"

@application.route('/', defaults={'path': 'myjavascript.html'})
@application.route('/<path:path>')
def proxy(path):
  return get(f'{SITE_NAME}{path}').content


@application.route('/ip')
def getIP():
    serverIP = get('http://api.ipify.org?format=json').content.decode(encoding='UTF-8')
    requestIP = "{'requestorIP':'"+request.remote_addr+"'}"
    result = "{'ipInformation':["+\
        serverIP+","+\
        requestIP+\
        "]}" 
    return result 

if __name__ == "__main__":
    application.run()