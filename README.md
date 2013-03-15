mimic
=====

Raspberry Pi Python project that reads 1 pixel of data from a webcam and outputs that pixel's color to an LED strip

Instructions
======
# install dependencies
# plug in webcam & connect LED strip
# run "sudo python mimic.py" (sudo is necessary to access the SPI hardware)

RPI Dependencies
=====
* AdaFruit Occidentalis v0.2 distribution - http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2
* Image Processing Python library - http://www.cl.cam.ac.uk/~db434/raspi/downloads/#packages (you can ignore any instructions related to bluetooth)

Troubleshooting
=====
Webcam
-----
If you want to test that your webcam is connected properly, install and run the following:

	sudo apt-get install guvcview
	guvcview
	
This should launch an app that lets you display your webcam with a number of different configurations (color mode, framerate, etc)

SPI
-----
This blog post has some information about enabling SPI on RPI - http://www.brianhensley.net/2012/07/getting-spi-working-on-raspberry-pi.html