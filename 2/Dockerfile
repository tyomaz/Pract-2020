FROM python:3.8

WORKDIR /PRACT 

RUN apt-get update 
RUN apt-get install -y python3-pip
RUN pip3 install matplotlib
RUN pip3 install influxdb

COPY task2/ /PRACT/task2 

CMD ["python3", "main.py"]
