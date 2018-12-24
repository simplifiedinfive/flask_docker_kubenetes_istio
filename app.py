# The Docker image contains the following code
from flask import Flask
import requests

import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>This is a simple flask app!</h3>"
    resp = requests.get("https://www.google.com")
    html+="<h3>received "+str(resp.status_code)+" from https google</h3>"
    resp = requests.get("http://time.jsontest.com/")
    html+="<h3>received "+str(resp.status_code)+" from http time.jsontest</h3>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)