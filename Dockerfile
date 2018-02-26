FROM python:3.6.1-alpine

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

RUN pip install flask


COPY app /usr/src/app

CMD python app.py