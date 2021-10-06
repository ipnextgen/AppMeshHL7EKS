import time
import socket
import requests
from flask import Flask, redirect, url_for, request

app = Flask(__name__)


def ingest_hl7():
    message = "Service is healthy"
    return message


@app.route('/hl7/<hl7msg>', methods = ['GET','POST'])
def hit(hl7msg):
    if request.method == 'GET':
        count = ingest_hl7()
        return "<html>HL7 Ingestion service on node %s.<br \>>Response : %s" % ( socket.gethostname(), count)
    
    if request.method == 'POST':
        datacontent = request.form
        r = requests.post("http://a8cf492c0594442729b248d1d207470b-1627855603.us-east-2.elb.amazonaws.com/hl7/store", data={'hl7': datacontent['hl7']})
        print(r.status_code, r.reason)
        return "<html>HL7 Ingestion service on node %s.<br \>>Response : %s <br \>>Status: %s <br \>>Reason: %s" % ( socket.gethostname(), datacontent, r.status_code, r.reason)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
