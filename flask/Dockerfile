FROM python:3.8-slim


COPY r.txt /
RUN pip install -r /r.txt

ADD . /flask
WORKDIR /flask

ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0 --port=80

