#!/usr/bin/env python
#coding: utf8

import os
import time
from neopixel import *
import argparse




LED_COUNT = 15
LED_PIN = 18
LED_FREQ_HZ = 80000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0


def lightup(strip, color, wait_ms):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(1)


