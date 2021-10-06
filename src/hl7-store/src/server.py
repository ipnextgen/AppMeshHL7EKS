import time
import socket
import requests
from flask import Flask, redirect, url_for, request

app = Flask(__name__)
# cache = redis.Redis(host='redis.internal-bookingapp.com', port=6379)


def ingest_hl7():
    message = "Ok"
    return message


@app.route('/hl7/<hl7msg>', methods = ['GET','POST'])
def hit(hl7msg):
    if request.method == 'GET':
        count = ingest_hl7()
        return "<html>HL7 Ingestion service on node %s.<br \>>Response : %s" % ( socket.gethostname(), count)
    
    if request.method == 'POST':
        data = request.form
        return "<html>HL7 Ingestion service on node %s.<br \>>Response : %s" % ( socket.gethostname(), data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
