#!/usr/bin/env python
#coding: utf8

import os
import time
from neopixel import *
import argparse
import numpy as np





LED_COUNT = 70
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 150
LED_INVERT = False
LED_CHANNEL = 0
SLEEPING = True
SLEEPING_counter = 0

# Define functions to change the LED colors
def lightup(strip, color=Color(255,0,0)):
    #LED after LED should lights up
    for i in range(strip.numPixels()):
        for j in range(strip.numPixels()):
            if(j<=i):
                strip.setPixelColor(j, color)
                strip.show()
        time.sleep(0.1)

def changeinstantfullcolor(strip, color):
    #Set Color of the full stripe to color
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(0.005)

def instant_shutdown(strip):
    #Instant put the LEDs off
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()

def read_config_file():
    power, auto, color, mode, show, intens, version = np.genfromtxt('/home/pi/LED-Project/config.txt', dtype='str')
    return np.array([power, auto, color, mode, show, intens, version])
            
def check_config_change(lastversion):
    file_version = read_config_file()[-1]
    if file_version == lastversion:
        return False
    else:
        return True

#Define differt Modi
def modi_gaming(strip):
    pass


def modi_wakeup(strip, color=Color(0,0,255)):
    lightup(strip, color)
    time.sleep(1200)


def modi_music(strip):
    pass

def modi_sleep(strip):
    instant_shutdown(strip)
    

def color_table(color):
    #Give color string return Color
    if color == 'GREEN':
        return Color(255,0,0)
    elif color == 'RED':
        return Color(0,255,0)
    elif color == 'BLUE':
        return Color(0,0,255)
    else:
        return Color(255,255,255)


#function to check if my gaming PC is running
def check_pconline(pc='192.168.0.234'):
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
    config = read_config_file()
    lightup(strip, Color(255,255,255))
    modi_sleep(strip)


    # Old Main Programm Loop
    #while True:
    #
    #   if time.strftime('%w') < 6 and time.strftime('%w') != '0':
    #       if time.strftime('%H') == '6' and time.strftime('%M') > 15 and time.strtime('%M') < 35:
    #           modi_wakeup(strip)
    #   #Check if PC is running
    #   elif check_pconline() is True:
    #       if SLEEPING is True:
    #           SLEEPING = False
    #           SLEEPING_counter = 0
    #           lightup(strip)
    #       else:
    #           time.sleep(30)
    #   else:
    #       if SLEEPING is True:
    #           pass
    #       else:
    #           if SLEEPING_counter < 2:
    #               SLEEPING_counter = SLEEPING_counter + 1
    #               pass
    #           else:
    #               SLEEPING = True
    #               modi_sleep(strip)

#Main Programm Loop
    while True:
        if check_config_change(config[-1]) == True:
            # Config changed since last check
            new_config = read_config_file()
            if new_config[0] == '0':
                #Led are off
                if SLEEPING == True:
                    #Led are off
                    pass
                else:
                    #Led are on
                    SLEEPING = True
                    config[0] = 0
                    config[-1] = new_config[-1]
                    modi_sleep(strip)
            else:
                #Led are on
                if new_config[1] == config[0]:
                    # Automatic is the same as Last check
                    pass
                else:
                    #Automatic mode changed
                    config[1] = new_config[1]
                    config[-1] = new_config[-1]

                if new_config[2] == config[2]:
                    #color is the same al last check
                    pass
                else:
                    #color changed
                    config[2] = new_config[2]
                    changeinstantfullcolor(strip, color_table(config[2]))
                    config[-1] = new_config[-1]

                if new_config[3] == config[3]:
                    #mode is the same as last check
                    pass
                else:
                    #mode changed
                    config[3] = new_config[3]
                    config[-1] = new_config[-1]

                if new_config[4] == config[4]:
                    #Show is the same as last check
                    pass
                else:
                    #Show changed 
                    config[4] = new_config[4]
                    config[-1] = new_config[-1]

                if new_config[5] == config[5]:
                    #Intens is the same as last check
                    pass
                else:
                    #Intens changed
                    config[5] = new_config[5]
                    config[-1] = new_config[-1]
        else:
             #Config didn't changed since last check
            if config[0] == '1':
                #Power on
                if config[1] == '1':
                    #Automatic on
                    if check_pconline() == True:
                        #Pc is online
                        if SLEEPING is True:
                            #Led are Sleeping
                            SLEEPING = False
                            SLEEPING_counter = 0
                            lightup(strip,color_table(config[2]))
                        else:
                            #Led are on
                            pass
                    elif time.strftime('%w') < '6' and time.strftime('%w') != '0' and time.strftime('%H') == '6' and time.strftime('%M') > '15' and time.strtime('%M') < '35':
                        #Its between Mon-Fr
                        #Its between 6:15 and 6:35
                        modi_wakeup(strip)
                    else:
                        #no Automatic condition fullfilled
                        if SLEEPING is True:
                            #Led are Sleeping
                            pass
                        else:
                            #Led are on
                            if SLEEPING_counter < 6:
                                #Less than 6 Sleeping Loops
                                SLEEPING_counter = SLEEPING_counter + 1
                                pass
                            else:
                                #More than 6 Sleeping Loops
                                SLEEPING = True
                                modi_sleep(strip)
            else:
                #Power off
                pass
        time.sleep(1)





            





  
 
      


 
