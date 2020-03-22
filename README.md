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
Go to the home directory using and create a folder called automationScripts
    ```cd ```
    ```mkdir automationScripts```
    ```cd automationScripts```
    

