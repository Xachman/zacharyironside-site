FROM python:3.6.1-alpine

ARG DEV
ENV DEV=${DEV}

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

RUN pip install flask

COPY app /usr/src/app

RUN if [[ "$DEV" = "true" ]]; then \
apk add --update nodejs &&  \
npm install -g gulp && \
npm install; \
fi



CMD python app.py