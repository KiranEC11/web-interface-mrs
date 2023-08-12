FROM ubuntu:18.04

RUN apt update && apt install -y build-essential libssl-dev libffi-dev python3-dev python3-pip

COPY requirements.txt /usr

RUN cd /usr && pip3 install -r requirements.txt
# RUN cd MRS_content/ && python3 manage.py runserver