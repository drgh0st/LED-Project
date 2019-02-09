#!/usr/bin/env python
#coding: utf8

import os
import time
from neopixel import *
import argparse





LED_COUNT = 70
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 150
LED_INVERT = False
LED_CHANNEL = 0


# Define functions to change the LED colors
def lightup(strip, color=Color(255,0,0)):
	#LED after LED should lights up
	for i in range(strip.numPixels()):
		for j in range(strip.numPixels()):
			if(j<=i):
				strip.setPixelColor(j, color)
				strip.show()
		time.sleep(0.25)

def changeinstantfullcolor(strip, color)
	#Set Color of the full stripe to color
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(0.005)


				


#Define differt Modi
def modi_gaming(strip):
	pass


def modi_wakeup(strip, color=Color(0,0,255)):
	pass

def modi_music(strip):
	pass




#function to check if my gaming PC is running
def check_pconline(pc=192.168.0.234):
	if os.system("ping -c 1 " + pc) == 0:
		return True
	else:
		return False



# Main program logic follows:
if __name__ == '__main__':

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    #startup sequenze
    lightup(strip)

    #Main Programm Loop
    while True:
    	#Check if PC is running
    	if check_pconline() is True:
    		modi_gaming(strip)
    	else
    		pass





  
 
      


 
