import RPi.GPIO as IO
import time
import subprocess

#import os

IO.setmode(IO.BCM)
IO.setup(21,IO.OUT)

#Monitoring if Temperatur exceeds 50 Degree Celcius

while (True):
	time.sleep(1)
	temp =  subprocess.check_output(['vcgencmd", " measure_temp'])
	print(temp)
	if(temp > 50.0):
		IO.output(21,True)
		print("Temp is higher than 50 deg")
	else:
		IO.output(21,False)
		print("Temp is lower than 50 deg")
