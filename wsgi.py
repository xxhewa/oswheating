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

    result = "Hello World on Openshift, here are the temperatures:<br>"
    result = result + "Temperature 1: "+str(temperature1)+ " °C<br>"
    result = result + "Temperature 2: "+str(temperature2)+ " °C<br>"
    result = result + "Temperature 3: "+str(temperature3)+ " °C<br>"
    result = result + "Temperature 4: "+str(temperature4)+ " °C<br>" 
    return result

@application.route("/metrics")
def monitor():

    result = ""
    result = result + "Temperature_1 "+str(temperature1)+"\n"
    result = result + "Temperature_2 "+str(temperature2)+"\n"
    result = result + "Temperature_3 "+str(temperature3)+"\n"
    result = result + "Temperature_4 "+str(temperature4)+"\n"
    return result

@application.route("/push/", methods=['POST'])
def push():

    # using global variables for changing the values
    global temperature1
    global temperature2
    global temperature3
    global temperature4

    temperature1 = float(request.form.get('temperature1'))
    temperature2 = float(request.form.get('temperature2'))
    temperature3 = float(request.form.get('temperature3'))
    temperature4 = float(request.form.get('temperature4'))
    return "got it...:"+str(temperature1)+";"+str(temperature2)+";"+str(temperature3)+";"+str(temperature4)

if __name__ == "__main__":
    application.run()