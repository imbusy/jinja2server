#!/usr/bin/env bash

# fix some issue with docker crashing on startup
curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker vagrant

printf "\nREGISTRATOR_IP=10.0.2.15\nDOCKER_IP=172.17.0.1\n" >> /etc/environment

echo Welcome to your new home!
