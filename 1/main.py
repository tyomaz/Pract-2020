from influxdb import InfluxDBClient
import random
import time

client = InfluxDBClient(host = 'localhost', port = 8086)
client.create_database('pract')
client.switch_database('pract')

VAL = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

fields = {x: 0 for x in VAL}

client.drop_measurement("events")

countStr = input("Введите количество итераций: ")
count = int (countStr)

i = 0
while (i < count):
    i += 1
    client.write_points([
        {
            "measurement": "events",
            "fields": fields 
        }
    ])

    for a in fields:
        fields[a] = fields[a] + random.randint(-2, 2)
    time.sleep(1)