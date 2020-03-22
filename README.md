# labPi
Everything about setting up my labPi.

## Installing the OS
Download Raspian-lite and write it to the SD-Card  
[Raspberry Pi Downloads](https://www.raspberrypi.org/downloads/raspbian/ "raspberrypi.org")

## First boot
Copy the files from the ___first_boot___-folder to the boot partition of the SD-Card.  
Open the ___wpa_supplicant.conf___ and replace the SSID and the password.

## First login
Open a CMD and type "ssh pi@192.168.0.???" and enter the password  
Create a folder called ___.ssh___ using
```mkdir .shh```  
```cd .shh```  
```nano authorized_keys```  
Copy yout public ssh-key into this file. Then save and close it. Now ssh-login without password works.

## Important scripts
Go to the home directory using and create a folder called ___automationScripts___:
```cd ```  
```mkdir automationScripts```  
```cd automationScripts```  
Create the according python files using the names from the files in ***pi/automationScripts***:  
```nano filename.py```   
Copy the content into the file. Save and close it. Repeat it for all the scripts.

## Installing the required programs
First update and upgrade the system using
```sudo apt-get update```  
```sudo apt-get upgrade```  
Then install mosquitto and pip
```sudo apt-get install mosquitto mosquitto-clients python-pip```  
Next, install the paho-mqtt python library globally  
```sudo -H pip install paho-mqtt```  

## Creating a systemd-entry for the mqttShutdown-Script
To create a new systemd entry just enter the following command:  
```sudo nano /etc/systemd/system/mqttShutdown.service```
Copy and paste the content from ***mqttShudown_systemd.txt***
Then save this file and execute following commands:
```sudo systemd daemon-reload```  
```sudo systemd enable mqttShutdown.service```  
```sudo systemd start mqttShutdown.service```

## Setting the for daily shutdown
Finally, to enable automatic shutdown every evening (22:30) create a cronjob using  
```sudo nano /etc/crontab```  
At the end of the file paste the content from ***crontab_entry.txt***. Save and close the file.  
FINISHED!


