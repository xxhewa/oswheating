import os
import json
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    data = os.environ['db2-cred']
    print('data1:',data)
    data = json.loads(data)
    print('data1:',data)
    return "OpenShift Hello World 4!"

@application.route("/cars")
def cars():
    data = '{"imageList": [\
   {"url":"test1.jpg","time":"25.02.2020 15:07"},\
   {"url":"test2.jpg","time":"25.02.2020 15:11"},\
   {"url":"test3.jpg","time":"25.02.2020 15:22"},\
   {"url":"test4.jpg","time":"26.02.2020 15:25"} \
   ]}'
    return data

if __name__ == "__main__":
    application.run()