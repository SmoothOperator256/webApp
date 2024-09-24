# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# Update system
RUN apt-get update
RUN apt-get upgrade -y

# Prevent the installation to hang
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get install -y \
python3 \
python3-pip
RUN pip install Flask
RUN pip install mysql-connector-python

# Install app

RUN mkdir /modules
RUN mkdir /static
RUN mkdir /templates

COPY app.py /
COPY modules /modules
COPY static /static
COPY templates /templates

EXPOSE 8000

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]


