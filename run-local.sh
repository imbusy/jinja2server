#/bin/bash
set +e
sudo docker stop jinja2server
sudo docker rm jinja2server
set -e

sudo docker run -it \
  -v /vagrant/templates:/home/web/templates \
  -v /vagrant/src:/home/web/src \
  -p 9000:8000 \
  --name jinja2server \
  jinja2server
