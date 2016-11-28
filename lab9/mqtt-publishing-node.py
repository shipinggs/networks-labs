# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client('python_pub')
mqttc.connect('scy-phy.net', 1337, 60)
mqttc.publish('hello/world', 'Hello, World!')
mqttc.loop(2) # timeout = 2s
