from waggle import plugin
from time import sleep
from pySMART import Device
import logging
import os
import json
import paho.mqtt.publish as publish

if(os.getenv('SAGE_DEBUG')):
    logging.basicConfig(level=logging.DEBUG)

nvmedev = os.getenv('NVME_DEVICE', "/dev/nvme0")
period = int(os.getenv('POLL_PERIOD', "60"))
topic = os.getenv("TOPIC", "/demo/nvmetemp_count")
mqttbrokerhost = os.getenv("MQTT_BROKER_HOST")

plugin.init()

while True:
    n = Device(nvmedev)
    print("publishing value", n.temperature)
    plugin.publish("sys.nvme.temperature", n.temperature)
    if mqttbrokerhost: 
        msg = { 'temp': n.temperature }
        print("fluent-bit logging: {}".format(msg), mqttbrokerhost, topic)
        publish.single(topic, json.dumps(msg), hostname=mqttbrokerhost)
    sleep(period)

