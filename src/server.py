import time
import socket
import requests
from flask import Flask

app = Flask(__name__)
# cache = redis.Redis(host='redis.internal-bookingapp.com', port=6379)


def ingest_hl7():
    message = "Ok"
    return message


@app.route('/home')
def hit():
    count = ingest_hl7()
    return "<html>HL7 Ingestion service on node %s.<br \>>Response : %s" % ( socket.gethostname(), count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
