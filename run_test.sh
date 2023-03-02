#!/bin/bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 --install --upgrade pip
pip install -r requirements.txt
python -m pytests test.py
echo "DONE!"
