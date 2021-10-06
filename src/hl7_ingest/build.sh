#!/bin/sh
docker build . -t hl7_ingest
docker tag hl7_ingest 279855623390.dkr.ecr.us-east-2.amazonaws.com/hl7_ingest
docker push 279855623390.dkr.ecr.us-east-2.amazonaws.com/hl7_ingest
