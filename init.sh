#!/usr/bin/env bash

rm -rf config
mkdir config
rm docker-compose.yml

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python generate_config.py

deactivate

docker-compose up $1