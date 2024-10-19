# DHT11 Sensor with MQTT Client for ThingSpeak
This is a MicroPython script that reads temperature and humidity data from a DHT11 sensor and publishes the data to ThingSpeak via MQTT. The script also controls an LED, turning it on when certain temperature or humidity thresholds are exceeded.

## Features
Wi-Fi Connection: The script connects the microcontroller to a Wi-Fi network using SSID and password.
DHT11 Sensor: Reads temperature and humidity data from the DHT11 sensor connected to a GPIO pin.
MQTT Client: Sends the sensor data to ThingSpeak using MQTT protocol.
Threshold-based LED Control: Turns on an LED if the temperature exceeds 30°C or humidity exceeds 70%.

## How It Works
Connects to the Wi-Fi using the provided SSID and password.
Continuously reads temperature and humidity data from the DHT11 sensor.
Publishes the sensor data to a ThingSpeak channel using MQTT.
Turns on an LED if the temperature is higher than 30°C or humidity is above 70%, otherwise the LED stays off.
Setup
Clone this repository and upload the script to your microcontroller (e.g., ESP8266/ESP32) running MicroPython.

## Replace the following placeholders in the script:

NETWORK NAME with your Wi-Fi SSID.

NETWORK PASSWORD with your Wi-Fi password.

YOUR CHANNEL with your ThingSpeak channel ID.

YOUR KEY with your ThingSpeak write API key.

Run the script on your microcontroller.

### Requirements
Microcontroller: ESP8266 or ESP32

Sensor: DHT11

### MicroPython Libraries:
dht

machine
network
umqtt.simple
