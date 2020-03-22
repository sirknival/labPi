#!/bin/sh

import paho.mqtt.client as mqtt
import RPi.GPIO as IO
import time
import os

#Declare topics for subsription
allTopics = "labPi/power"

#IO Stuff
IO.setmode(IO.BCM)
IO.setup(26,IO.OUT)
IO.output(26, True)
#Send shutdown command
def sendShutdownCmd ():
    IO.output(26, False)
    time.sleep(0.2)
    IO.output(26, True)
    time.sleep(0.2)
    os.system('sudo shutdown now "Cya later alligator"')

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    client.subscribe(allTopics)
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == allTopics:
        if msg.payload == 'True':
	    sendShutdownCmd()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.31", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
run = True
while run:
    client.loop_forever()



