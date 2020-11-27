# for flask: docker run --env-file=.flaskenv image flask run
FROM docker.cloudsmith.io/cloudsmith/challenges-pub/python:3.8

RUN mkdir /code
WORKDIR /code

COPY requirements.txt setup.py tox.ini ./
RUN pip install -r requirements.txt
RUN pip install -e .

COPY challenge challenge/
COPY migrations migrations/

EXPOSE 5000
