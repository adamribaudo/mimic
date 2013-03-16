mimic
=====

Raspberry Pi Python project that reads 1 pixel of data from a webcam and outputs that pixel's color to an LED strip

Instructions
======
* install dependencies
* plug in webcam & connect LED strip
* run "sudo python mimic.py" (sudo is necessary to access the SPI hardware)

RPI Dependencies
=====
* AdaFruit Occidentalis v0.2 distribution - http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2
* Image Processing Python library - http://www.cl.cam.ac.uk/~db434/raspi/downloads/#packages (you can ignore any instructions related to bluetooth)

It's also recommend you run these, but they will take a while and I'm not sure if they're necessary:

	sudo apt-get clean
	sudo apt-get update
	sudo apt-get upgrade
	apt-get install libmpg123-dev gstreamer0.10-nice gstreamer0.10-tools gstreamer0.10-plugins-good gstreamer0.10-plugins-bad gstreamer0.10-plugins-ugly gstreamer0.10-alsa
	apt-get install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libavcodec-dev libavformat-dev libavutil-dev libswscale-dev freeglut3-dev libasound2-dev libxmu-dev libxxf86vm-dev g++ libgl1-mesa-dev libglu1-mesa-dev libraw1394-dev libudev-dev libdrm-dev gstreamer0.10-ffmpeg libglew-dev libopenal-dev libsndfile-dev libfreeimage-dev libcairo2-dev libgtk2.0-dev libjack-jackd2-dev python-lxml python-argparse portaudio19-dev

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