# pi-vibration-sensor
Test Stand integration of a vibration SenseHat for Raspberry Pi

![img](https://img.shields.io/badge/build-beta-green) This seems to work okay.


## Installation 

From new flash card / Fresh RasPi Install
 - Create user with name "pi" and log in
 - sudo apt-get update
 - sudo apt-get install sense-hat nano
 - sudo reboot
 - copy this file (vibration.py) to /home/pi/
 - mkdir /home/pi/data/
 - nano /home/pi/.bashrc
 - Copy following code to the bottom of this file (shift+ins)
```
vibe() {
	python /home/pi/vibration.py
}
```
 - source /home/pi/.bashrc
 - vibe (starts test)

## Usage
1. To start test, type "vibe" into terminal window (login from windows command line with "ssh pi@ip_address_of_pi" or use Putty)

2. To end test, hit Ctrl+C OOOOOONCE (twice could/will corrupt current test)

3. To download data, use WinSCP to connect to Pi. Navigate to data folder; download, delete, whatever.

4. Filename is the current Unix epoch. use epochconverter.com to make it human-readable

## Debugging:
- Turn it off and on again?
