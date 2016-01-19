FROM ubuntu:wily
MAINTAINER Lukas Steiblys

RUN apt-get update
RUN apt-get install -y \
  gcc \
  python3 \
  python3-dev \
  wget

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip install uwsgi
RUN pip install jinja2

EXPOSE 8000

RUN useradd web

COPY src /home/web/src
WORKDIR /home/web/src

CMD ["uwsgi", "--http", ":8000", "--wsgi-file", "application.py", "--master", "--processes", "4", "--threads", "2"]
