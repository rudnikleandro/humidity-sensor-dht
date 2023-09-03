import dht
import machine
import time
import network
from umqtt.simple import MQTTClient

def connect(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

server = "mqtt.thingspeak.com"
client = MQTTClient ("umqtclient", server)
channel = "YOUR CHANNEL"
key = "YOUR KEY"
address = "channels/" + channel + "/publish/" + key
print("Connecting...")
wifi = connect("NETWORK NAME", "NETWORK PASSWORD")

while True:
    print("Measuring temperature and humidity...")
    d.measure()
    temperature = d.temperature()
    humidity = d.humidity()
    field = "field1={}&field2={}".format(temperature, humidity)
    
    client.connect()
    client.publish(address, field)
    client.disconnect()
    
    print("Temperature: {}°C Humidity: {}%".format(d.temperature(), d.humidity()))

    if (d.temperature()>30) or (d.humidity()>70):
        r.value(1)
    else:
        r.value(0)
    time.sleep(3)