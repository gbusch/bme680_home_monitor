# Code for ESP8266 (deprecated)

At first, I used an ESP8266 microcontroller. The code that I used can be found in this directory. However, here the Arduino IDE is used to flash the controller (note the *.ino file). 

I tried to switch to platform.io since this allows to include all dependencies as well. Unfortunately, there was still manual configuration necessary. Namely, the linker script had to be adjusted as described [on the library's Github page](https://github.com/BoschSensortec/BSEC-Arduino-library#4-additional-core-specific-modifications). After many (unsuccessful) tries to include a modified version of this linker script in the project, I decided to switch to an ESP32 where the configuration with platform.io is straight-forward.

If you want to use an ESP8266, these files might help. Please note that the protobuf message format has changed in the meantime and has to be adjusted (in the mqtt-forwarder).