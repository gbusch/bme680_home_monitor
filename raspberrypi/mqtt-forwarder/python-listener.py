import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import datetime
import json
import logging
import os

import data_pb2
import google.protobuf


def persist(msg):
    data = data_pb2.WeatherData()
    try:
        data.ParseFromString(msg.payload)
        current_time = datetime.datetime.utcnow().isoformat()
        json_body = [
            {
                "measurement": "weather",
                "tags": {"location": "bedroom"},
                "time": current_time,
                "fields": {
                    "temperature": float(data.temperature),
                    "humidity": float(data.humidity),
                    "pressure": int(data.pressure),
                    "IAQ": float(data.IAQ)
                }
            }
        ]
        print(json_body)
        influx_client.write_points(json_body)
    except google.protobuf.message.DecodeError:
        print(msg.topic+" Expected WeatherData but got: "+str(msg.payload))
    except:
        print("other error")

logging.basicConfig(level=logging.INFO)
influx_client = InfluxDBClient('influxdb', 8086, database=os.environ["INFLUXDB_DB"].strip(), username=os.environ["INFLUXDB_USER"].strip(), password=os.environ["INFLUXDB_USER_PASSWORD"].strip())
client = mqtt.Client()

client.on_connect = lambda self, mosq, obj, rc: self.subscribe("/weather/bedroom")
client.on_message = lambda client, userdata, msg: persist(msg)

client.connect("mqtt", 1883, 60)
client.loop_forever()
