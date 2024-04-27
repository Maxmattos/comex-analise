FROM python:latest

RUN mkdir data-case

WORKDIR /home/data-case

COPY requirements.txt .

RUN pip install -r requirements.txt