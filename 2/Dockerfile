FROM python:3.8

WORKDIR /PRACT 

RUN apt-get update 
RUN apt-get install -y python3-pip
RUN pip3 install matplotlib
RUN pip3 install influxdb

COPY 2/ /PRACT/2

CMD ["python3", "main.py"]
