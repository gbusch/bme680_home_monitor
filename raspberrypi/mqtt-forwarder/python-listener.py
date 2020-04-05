import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import datetime
import json
import logging
import os

def persist(msg):
    data = json.loads(msg.payload.decode("utf-8"))
    print(data)
    current_time = datetime.datetime.utcnow().isoformat()
    json_body = [
        {
            "measurement": "weather",
            "tags": {"location": "bedroom"},
            "time": current_time,
            "fields": data
        }
    ]
    influx_client.write_points(json_body)

logging.basicConfig(level=logging.INFO)
influx_client = InfluxDBClient('influxdb', 8086, database=os.environ["INFLUXDB_DB"].strip(), username=os.environ["INFLUXDB_USER"].strip(), password=os.environ["INFLUXDB_USER_PASSWORD"].strip())
client = mqtt.Client()

client.on_connect = lambda self, mosq, obj, rc: self.subscribe("/weather/bedroom")
client.on_message = lambda client, userdata, msg: persist(msg)

client.connect("mqtt", 1883, 60)
client.loop_forever()
