#!/bin/sh
docker build . -t hl7_ingest
#docker tag hl7_ingest 279855623390.dkr.ecr.us-east-2.amazonaws.com/hl7_ingest
#docker push 279855623390.dkr.ecr.us-east-2.amazonaws.com/hl7_ingest
docker tag hl7_ingest public.ecr.aws/d9m0n6d3/hl7_ingest
docker push public.ecr.aws/d9m0n6d3/hl7_ingest