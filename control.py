import numpy as np
from optparse import OptionParser
from helper import assist_functions as af
import os


def led_stripes_on():
	pass

def led_stripes_off():
	pass

def led_automatic_on():
	pass

def led_automatic_off():
	pass

def led_mode_gaming():
	pass

def led_mode_music():
	pass

def led_mode_custom():
	pass

def led_bright_up():
	pass

def led_bright_down():
	pass

def led_color_red():
	pass

def led_color_green():
	pass

def led_color_blue():
	pass

def led_pattern_idle():
	pass

def led_pattern_wave():
	pass



if __name__ == '__main__':
    

    parser = OptionParser()
    parser.add_option('-o', '--operation', type='string', dest='operation')
    (options, args) = parser.parse_args()

    
    operation = options.operation

    if operation == 'lsn':
    	led_stripes_on()
    elif operation == 'lsf':
    	led_stripes_off()
    elif operation == 'lan':
    	led_automatic_on()
    elif operation == 'laf':
    	led_automatic_off()
    elif operation == 'lmg':
    	led_mode_gaming()
    elif operation == 'lmm':
    	led_mode_music()
    elif operation == 'lmc':
    	led_mode_custom()
    elif operation == 'lbu':
    	led_bright_up()
    elif operation == 'lbd':
    	led_bright_down():
    elif operation == 'lcr':
    	led_color_red()
    elif operation == 'lcg':
    	led_color_green()
    elif operation == 'lcb':
    	led_color_blue()
    elif operation == 'lpi':
    	led_pattern_idle()
    elif operation == 'lpw':
    	led_pattern_wave()
    else:
    	print('Wrong Option.')
    	


    
   