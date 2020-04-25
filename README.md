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
This was realized with a BME680 sensor from Bosch connected to a ESP32 which is a powerful microcontroller with, amongst others, wifi connectivity. The backend and frontend run on a Raspberry Pi 3. As frontend we use Grafana which also allows for alerting, for example as Telegram notifications on the smart phone. The Grafana dashboard can be accessed from all devices which are connected to the home wifi network.

![image missing](./images/schematics.png "Schematics")

### Measuring and sending data with the ESP32
TBD

### Compiling the protocol buffers
TBD

### Processing, storing, and displaying data on the Raspberry Pi
TBD



## Shopping list
Here is a short overview of the parts that you will need:
* The BME680 sensor from Bosch Sensortec. You probably want to get a breakout board. I got the one from BlueDot. A soldering iron was needed to solder the 6-pin header to the board. There might be boards on the market that have the header already attached. Cost: around 20 €. (If you are not interested in indoor air quality but only temperature and humidity you might want to check out the BME280 which is available for less than 5 €.)
* An ESP32 microcontroller. I used the ESP32 Dev Kit C from az-delivery.de but there are many different versions on the market that should work as well. A ESP8266 can also be used but I failed to fully program it with platform.io without any manual modifications. Cost: around 10 €.
* Jumper wires (female-female) to connect ESP32 and sensor.
* A micro-USB phone charger to power the ESP32.
* A Raspberry Pi with (micro) SD card and power supply. I got an ABOX (now LABISTS) Raspberry Pi 3B+ starter kit which also contained case, power supply, heat sinks and SD card. Cost: around 85 €.
