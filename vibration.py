import time
from sense_hat import SenseHat
sense = SenseHat()
temperature = sense.get_temperature()
humidity = sense.get_humidity()

filename = "/home/pi/data/{}-{}C-{}%%rH.csv".format(time.time(),temperature,humidity)
f = open(filename, "w")

try:
	while True:
		orientation = sense.get_orientation()
		print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
		f.write("{pitch},{roll},{yaw}".format(**orientation))
except KeyboardInterrupt:
	f.close()


"""
Documentation:

To start test, type "vibe" into terminal window (login from windows command line with "ssh pi@ip_address_of_pi" or use Putty)
To end test, hit Ctrl+C OOOOOONCE (twice could/will corrupt current test)
To download data, use WinSCP to connect to Pi. Navigate to data folder; download, delete, whatever.

Filename is the current Unix epoch. use epochconverter.com to make it human-readable

From new flash card / Fresh RasPi Install
 - Create user with name "pi" and log in
 - sudo apt-get update
 - sudo apt-get install sense-hat nano
 - sudo reboot
 - copy this file (vibration.py) to /home/pi/
 - mkdir /home/pi/data/
 - nano /home/pi/.bashrc
 - Copy following code to the bottom of this file (shift+ins)

vibe() {
	python /home/pi/vibration.py
}

 - source /home/pi/.bashrc
 - vibe (starts test)

Debugging:
- Turn it off and on again

"""
