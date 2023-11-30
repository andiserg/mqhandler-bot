FROM python:3.10.12

ENV PYTHONUNBUFFERED 1

WORKDIR /mqhandlerbot

COPY . ./

RUN pip install -e .
