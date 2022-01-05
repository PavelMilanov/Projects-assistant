#!/bin/bash
echo "установка Python 3.10..."
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install -y python3.10 python3.10-distutils
echo "установка Git"
sudo apt install  -y git
echo "установка Python pip"
sudo apt install -y python3-pip
echo "установка poetry"
sudo pip3 install -y poetry
echo "настройка виртуального окружения poetry"
poetry config virtualenvs.in-project true
echo 'готово!'
