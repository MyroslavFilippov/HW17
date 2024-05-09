FROM ubuntu:latest

# Install necessary tools for attacks
RUN apt-get update
RUN apt-get upgrade
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install python3-scapy

# Copy attack scripts into the container
COPY attack_scripts /attack_scripts

WORKDIR /attack_scripts
