from imgproc import *
import LPD8806

print "Starting MIMIC..."
my_cam = Camera(320,240)
led = LPD8806.strand()

while 0 < 1:
	my_img = my_cam.grabImage()
	red, green, blue = my_img[160, 120]
	my_img[160, 120] = 0, 0, 0	
	led.fill(red, green, blue)
	
	
	
