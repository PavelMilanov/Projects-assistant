#!/bin/bash
echo "установка Python"
apt install -y python3
echo "установка Python pip"
apt install -y python3-pip
echo "установка poetry"
pip3 install poetry
echo "настройка виртуального окружения poetry"
poetry config virtualenvs.in-project true
