FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y python-pip
RUN rm -rf /var/lib/apt/lists/*

COPY webapp/REQUIREMENTS /app/REQUIREMENTS
WORKDIR /app/
RUN pip install -r REQUIREMENTS
RUN rm REQUIREMENTS
