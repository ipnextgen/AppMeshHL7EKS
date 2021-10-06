import time
import socket
import boto3
import requests
from flask import Flask, redirect, url_for, request

app = Flask(__name__)
# cache = redis.Redis(host='redis.internal-bookingapp.com', port=6379)

s3 = boto3.resource(
    's3',
    region_name='us-east-2'
)

def ingest_hl7():
    message = "Storing service is healthy"
    return message


@app.route('/hl7/<hl7msg>', methods = ['GET','POST'])
def hit(hl7msg):
    if request.method == 'GET':
        count = ingest_hl7()
        return "<html>HL7 Storing service on node %s.<br \>>Response : %s" % ( socket.gethostname(), count)
    
    if request.method == 'POST':
        content="String content to write to a new S3 file"
        s3.Object('hl7-storing-eks-demo-mglap', 'newfile.txt').put(Body=content)
        data = request.form
        return "<html>HL7 Storing service on node %s.<br \>>Response : %s" % ( socket.gethostname(), data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

