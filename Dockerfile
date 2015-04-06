FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python-pip python-dev python-psycopg2
RUN rm -rf /var/lib/apt/lists/*

COPY webapp/ /source/
WORKDIR /source/
RUN pip install -r REQUIREMENTS
RUN rm REQUIREMENTS

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser
