FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /main
WORKDIR /main

ADD requirements.txt /main/
RUN pip install -r requirements.txt

ADD . /main/