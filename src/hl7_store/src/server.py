import time
import socket
import boto3
import requests
import random
import string
import base64
from flask import Flask, redirect, url_for, request

app = Flask(__name__)
# cache = redis.Redis(host='redis.internal-bookingapp.com', port=6379)

s3 = boto3.resource(
    's3',
    region_name='us-east-2'
)

# Decoding Base64 and HL7
def ingest_hl7(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    # add hl7 logic here
    return message


@app.route('/hl7/<hl7msg>', methods = ['GET','POST'])
def hit(hl7msg):
    if request.method == 'GET':
        return "<html>HL7 Storing service is healthy on node %s.<br \>" % ( socket.gethostname())
    
    if request.method == 'POST':
        
        # Generating oject name randomly
        letters = string.ascii_lowercase
        objectname = ( ''.join(random.choice(letters) for i in range(10)) )
        
        # Decoding and Storing content
        data = request.form
        content = ingest_hl7(str(data['hl7']))
        s3.Object('hl7-storing-eks-demo-mglap', objectname).put(Body=content)
        
        # final return
        return "<html>HL7 Storing service on node %s.<br \>>Response : %s" % ( socket.gethostname(), data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


