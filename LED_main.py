#!/usr/bin/env python
#coding: utf8

import os
import time
from neopixel import *
import argparse





LED_COUNT = 16
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 150
LED_INVERT = False
LED_CHANNEL = 0


def lightup(strip, color=Color(255,0,0)):
	#LED after LED should lights up
	for i in range(strip.numPixels()):
		for j in range(strip.numPixels()):
			if(j<=i):
				strip.setPixelColor(j, color)
				strip.show()
				time.sleep(0.5)


# Main program logic follows:
if __name__ == '__main__':

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    #startup sequenze
    lightup(strip)
    

  
 
      


 
