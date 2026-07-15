FROM python:3.11-slim@sha256:9c7ae9f5568297b715978a6358edfaaa58d3419bb9557f62e873a4b0d0ed3fb1

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log