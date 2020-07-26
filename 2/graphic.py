import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from influxdb import InfluxDBClient

VAL = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

client = InfluxDBClient(host='localhost', port=8086)
q = client.query('SELECT * FROM "pract"."autogen"."events"', epoch='s')

p = q.get_points()
points = [x for x in p]

fields = {x: [] for x in VAL}
time = []

for i in range(len(points)):
    time.append(points[i].get('time'))
    for a in VAL:   
        fields[a].append(points[i].get(a))
    
def animate(i):   
    
    plt.cla()
    for a in VAL:
        plt.plot(time, fields[a], label=a)

    plt.legend(loc='lower left')

ani = FuncAnimation(plt.gcf(), animate)
plt.show()