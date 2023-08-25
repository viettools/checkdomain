FROM python:3.10

# Make Dir
RUN mkdir -p /data/checkdomain

# Copy all to new dir
COPY . /data/checkdomain

WORKDIR /data/checkdomain

RUN apt-get update && apt-get upgrade -y

RUN pip3 install --no-cache-dir -r /data/checkdomain/requirements.txt