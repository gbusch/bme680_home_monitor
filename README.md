# Indoor air quality monitoring

## Goal
My goal was to monitor temperature, humidity and indoor air quality (IAQ) in our apartment and display it in a dashboard which should be accessible from within our home network.

## Additional technical requirements
Additional requirements, which were mostly not practically necessary but rather added for educational purposes, where:
* communication between microcontroller and Raspberry Pi with MQTT
* MQTT messages are encoded in protocol buffer (protobuf) format
* software on microcontroller should be fully version controlled, including dependencies
* software on Raspberry Pi should be fully version controlled as well, including all configurations, and all software should be started with one command.

## Realization
This was realized with a BME680 sensor from Bosch connected to a ESP32 which is a powerful microcontroller with, amongst others, wifi connectivity. The backend and frontend run on a Raspberry Pi 3. As frontend we use Grafana which also allows for alerting, for example as Telegram notifications on the smart phone.

![image missing](./images/schematics.png "Logo Title Text 1")