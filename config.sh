#!/bin/bash
echo "установка Python 3.10..."
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install -y python3.10 python3.10-distutils
echo "установка Git"
sudo apt install  -y git
echo "установка Python pip"
sudo apt install -y python3-pip
echo "установка poetry"
sudo pip3 install poetry
echo "настройка виртуального окружения poetry"
poetry config virtualenvs.in-project true
echo "установка NodeJS 16.x"
url=https://deb.nodesource.com/setup_16.x 
curl -sL {{url}} -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install -y nodejs
sudo remove nodesource_setup.sh
sudo apt install -y npm
echo 'готово!'
python3.10 --version
git --version
poetry --version
node -v
npm -v
