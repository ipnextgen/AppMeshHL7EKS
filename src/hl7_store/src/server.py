import time
import socket
import boto3
import requests
import random
import string
import base64
import hl7
import os
from flask import Flask, redirect, url_for, request

app = Flask(__name__)
# cache = redis.Redis(host='redis.internal-bookingapp.com', port=6379)

s3 = boto3.resource(
    's3',
    region_name='us-east-2'
)

# Decoding Base64 and HL7
def ingest_hl7(base64_message):

    #base64_bytes = base64_message.encode('utf-8')
    #message_bytes = base64.b64decode(base64_bytes)
    #message = message_bytes.decode('utf-8')

    ## HL7
    message = 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\r'
    message += 'PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|196203520|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\r'
    message += 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||200202150730||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\r'
    message += 'OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F\r'
    
    h = hl7.parse(message)
    hl7_message = "'%s','%s'" % (str(h.segment('PID')[6][0]),str(h.segment('PID')[11][0]))
    return hl7_message

@app.route('/hl7/<hl7msg>', methods = ['GET','POST'])
def hit(hl7msg):
    if request.method == 'GET':
        return "<html>HL7 Storing service is healthy on node %s.<br \>" % ( socket.gethostname())
    
    if request.method == 'POST':
        
        # Generating oject name randomly
        letters = string.ascii_lowercase
        objectname = "%s.csv" % ( ''.join(random.choice(letters) for i in range(10)))
        
        # Decoding and Storing content
        data = request.form
        content = ingest_hl7(str(data['hl7']))
        s3.Object('hl7-storing-eks-demo-mglap', objectname).put(Body=content)
        
        # final return
        return "<html>HL7 Storing service on node %s.<br \>>Response : %s" % ( socket.gethostname(), data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)