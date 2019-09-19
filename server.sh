#!/bin/bash

PYTHONDONTWRITEBYTECODE=" " \
FLASK_DEBUG=1 \
FLASK_APP=app/app:app \
MONGODB_URL='mongodb://localhost:27017/test' \
SECRET_KEY='1234567890' \
flask run --port 8080
