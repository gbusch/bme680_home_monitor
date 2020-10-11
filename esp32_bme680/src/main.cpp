/* 
 * Example script for Bosch BSEC library
 * modified to publish data via MQTT
 * 
 * Copyright (C) 2017 Robert Bosch. All Rights Reserved. 
 */

#include <Arduino.h>

#include "bsec.h"
#include "credentials.h"

#include "WiFi.h"
#include <PubSubClient.h>

#include "data.pb.h"
#include <pb.h>
#include <pb_encode.h>

// Helper functions declarations
void checkIaqSensorStatus(void);
void mqtt_reconnect(void);

// Create an object of the class Bsec
Bsec iaqSensor;

String output;
int Nmeasure;

WiFiClient espClient;
PubSubClient client(espClient);

//for watchdog
#include "esp_system.h"
const int loopTimeCtl = 0;
hw_timer_t *timer = NULL;
const int watchdogTimeoutUs = 30000000; //in usec

void IRAM_ATTR resetModule()
{
  ets_printf("reboot\n");
  esp_restart();
}

void feedWatchdog()
{
  timerWrite(timer, 0); //reset timer (feed watchdog)
}

// Entry point for the example
void setup(void)
{
  Serial.begin(115200);
  Wire.begin(16, 17);

  //setup watchdog early to allow trigger even during setup
  timer = timerBegin(0, 80, true); //timer 0, div 80
  timerAttachInterrupt(timer, &resetModule, true);
  timerAlarmWrite(timer, watchdogTimeoutUs, false); //set time in us
  timerAlarmEnable(timer);                          //enable interrupt

  Serial.print("## Connecting to WiFi ##");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connented to Wifi with local IP: ");
  Serial.println(WiFi.localIP());

  client.setServer(mqttServer, mqttPort);

  iaqSensor.begin(BME680_I2C_ADDR_SECONDARY, Wire);
  output = "\nBSEC library version " + String(iaqSensor.version.major) + "." + String(iaqSensor.version.minor) + "." + String(iaqSensor.version.major_bugfix) + "." + String(iaqSensor.version.minor_bugfix);
  Serial.println(output);
  checkIaqSensorStatus();

  bsec_virtual_sensor_t sensorList[10] = {
      BSEC_OUTPUT_RAW_TEMPERATURE,
      BSEC_OUTPUT_RAW_PRESSURE,
      BSEC_OUTPUT_RAW_HUMIDITY,
      BSEC_OUTPUT_RAW_GAS,
      BSEC_OUTPUT_IAQ,
      BSEC_OUTPUT_STATIC_IAQ,
      BSEC_OUTPUT_CO2_EQUIVALENT,
      BSEC_OUTPUT_BREATH_VOC_EQUIVALENT,
      BSEC_OUTPUT_SENSOR_HEAT_COMPENSATED_TEMPERATURE,
      BSEC_OUTPUT_SENSOR_HEAT_COMPENSATED_HUMIDITY,
  };

  iaqSensor.updateSubscription(sensorList, 10, BSEC_SAMPLE_RATE_LP);
  checkIaqSensorStatus();

  // Print the header
  output = "Timestamp [ms], raw temperature [°C], pressure [hPa], raw relative humidity [%], gas [Ohm], IAQ, IAQ accuracy, temperature [°C], relative humidity [%], Static IAQ, CO2 equivalent, breath VOC equivalent";
  Serial.println(output);
}

// Function that is looped forever
void loop(void)
{
  unsigned long time_trigger = millis();
  if (iaqSensor.run())
  { // If new data is available
    output = String(time_trigger);
    output += ", " + String(iaqSensor.rawTemperature);
    output += ", " + String(iaqSensor.pressure);
    output += ", " + String(iaqSensor.rawHumidity);
    output += ", " + String(iaqSensor.gasResistance);
    output += ", " + String(iaqSensor.iaq);
    output += ", " + String(iaqSensor.iaqAccuracy);
    output += ", " + String(iaqSensor.temperature);
    output += ", " + String(iaqSensor.humidity);
    output += ", " + String(iaqSensor.staticIaq);
    output += ", " + String(iaqSensor.co2Equivalent);
    output += ", " + String(iaqSensor.breathVocEquivalent);
    // onboard LED blinks at every serial print, this is annoying, therefore commented out here.
    // Serial.println(output);
    Nmeasure++;

    if (Nmeasure == 5)
    {
      if (!client.connected())
      {
        delay(3000);
        mqtt_reconnect();
      }

      WeatherData data = WeatherData_init_zero;
      data.deviceId = 1;
      data.temperature = iaqSensor.temperature;
      data.humidity = iaqSensor.humidity;
      data.pressure = iaqSensor.pressure / 100.;
      data.IAQ = iaqSensor.iaq;
      data.iaq_accuracy = iaqSensor.iaqAccuracy;
      data.CO2 = iaqSensor.co2Equivalent;
      data.breath_VOC = iaqSensor.breathVocEquivalent;

      uint8_t buffer[64];
      pb_ostream_t stream = pb_ostream_from_buffer(buffer, sizeof(buffer));

      if (!pb_encode(&stream, WeatherData_fields, &data))
      {
        Serial.println("failed to encode temp proto");
      }
      else
      {
        client.publish("/weather/bedroom", buffer, stream.bytes_written);
      }
      Nmeasure = 0;
    }
  }
  else
  {
    checkIaqSensorStatus();
  }

  sleep(3);
}

// Helper function definitions
void checkIaqSensorStatus(void)
{
  if (iaqSensor.status != BSEC_OK)
  {
    if (iaqSensor.status < BSEC_OK)
    {
      output = "BSEC error code : " + String(iaqSensor.status);
      Serial.println(output);
    }
    else
    {
      output = "BSEC warning code : " + String(iaqSensor.status);
      Serial.println(output);
    }
  }

  if (iaqSensor.bme680Status != BME680_OK)
  {
    if (iaqSensor.bme680Status < BME680_OK)
    {
      output = "BME680 error code : " + String(iaqSensor.bme680Status);
      Serial.println(output);
    }
    else
    {
      output = "BME680 warning code : " + String(iaqSensor.bme680Status);
      Serial.println(output);
    }
  }
}

void mqtt_reconnect(void)
{
  while (!client.connected())
  {
    if (!client.connect("ESP32Client"))
    {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" retrying in 5 seconds");
      delay(500);
    }
  }
}
