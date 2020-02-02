from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "OpenShift Hello World 3!"

@application.route("/cars")
def hello():
    return '["test1.jpg", "test2.jpg", "test3.jpg"]'

if __name__ == "__main__":
    application.run()