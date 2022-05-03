#!/usr/bin/bash

#3.8.13

yum update -y

yum install gcc openssl-devel bzip2-devel libffi-devel wget -y

wget https://www.python.org/ftp/python/3.8.13/Python-3.8.13.tgz
tar xvf Python-3.8.13.tgz

cd Python-3.8.13/
./configure --enable-optimizations
make altinstall

cd ../
rm Python-3.8.13.tgz
rm -R Python-3.8.13/

pip3.8 install --user virtualenv

python3.8 -m virtualenv app

source app/bin/activate
pip install ansible-core==2.11.11
# ansible-galaxy collection install community.docker
