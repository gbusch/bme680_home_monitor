# Code for ESP8266 (deprecated)

At first, I used an ESP8266 microcontroller. The code that I used can be found in this directory. However, here the Arduino IDE is used to flash the controller (note the *.ino file). 

I tried to switch to platform.io since this allows to include all dependencies as well. Unfortunately, there was still manual configuration necessary. Namely, the linker script had to be adjusted as described [on the library's Github page](https://github.com/BoschSensortec/BSEC-Arduino-library#4-additional-core-specific-modifications). After many (unsuccessful) tries to include a modified version of this linker script in the project, I decided to switch to an ESP32 where the configuration with platform.io is straight-forward.

If you want to use an ESP8266, these files might help but they will not work straight away. More information on how to get the BSEC software running on ESP8266 can be found [on the library's github page](https://github.com/BoschSensortec/BSEC-Arduino-library#instructions-for-using-the-bsec-arduino-library-in-arduino-189).

Please note that the protobuf message format has changed in the meantime and has to be adjusted (in the mqtt-forwarder).

Also you will have to add your network configuration in [esp8266_bme680.ino]():
```C
const char* ssid = ## your wifi name here ##;
const char* password = ## your wifi password here ##;
const char* mqttServer = ## your MQTT brokers (raspberry pi) address ##;
const int mqttPort = 1883;
```

*Note: Most software in this folder is provided by Bosch Sensortec and only slightly modified. All rights remain at Bosch Sensortec.*