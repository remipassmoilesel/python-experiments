#!/usr/bin/env bash

set -e

echo
echo "Installing python virtual environment ..."
echo

python3.6 -m venv .venv
source .venv/bin/activate

pip3 install pip --upgrade
pip3 install -r requirements.txt
