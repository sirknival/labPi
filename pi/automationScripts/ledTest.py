#!bin/bash
import RPi.GPIO as GPIO
import time

# Variables
time_delay = 0.2
pins = [16,19,20,21,26]

# General GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Init GPIO Pins
for pin in pins:
    GPIO.setup(pin,GPIO.OUT)

#Start Test Procedure
for pin in pins:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(time_delay)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(time_delay)
# Clean GPIO use
for pin in pins:
    GPIO.cleanup(pin)
