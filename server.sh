#!/bin/bash

PYTHONDONTWRITEBYTECODE=" " \
FLASK_DEBUG=1 \
FLASK_APP=app.py \
MONGODB_URL='mongodb://localhost:27017/test' \
SECRET_KEY='1234567890' \
flask run --host 0.0.0.0 --port 8080
