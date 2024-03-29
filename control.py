import numpy as np
from optparse import OptionParser
import os


def led_stripes_on(config): 
    if config[0] == '0':
        config[-1] = str(int(config[-1]) + 1)
        config[0] = 1 
        write_config_file(config)
    else:
        pass

def led_stripes_off(config):
    if config[0] == '1':
        config[-1] = str(int(config[-1]) + 1)
        config[0] = 0 
        write_config_file(config)
    else:
        pass

def led_automatic_on(config):
    if config[1] == '0':
        config[-1] = str(int(config[-1]) + 1)
        config[1] = 1 
        write_config_file(config)
    else:
        pass
def led_automatic_off(config):
    if config[1] == '1':
        config[-1] = str(int(config[-1]) + 1)
        config[1] = 0 
        write_config_file(config)
    else:
        pass

def led_mode_gaming(config):
    if config[3] == 'GAMING':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[3] = 'GAMING' 
        write_config_file(config)

def led_mode_music(config):
    if config[3] == 'MUSIC':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[3] = 'MUSIC' 
        write_config_file(config)

def led_mode_custom(config):
    if config[3] == 'CUSTOM':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[3] = 'CUSTOM' 
        write_config_file(config)

def led_bright_up(config):
    if int(config[5]) > 250:
        #if value would be out of bounds dont do it
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[5] = str(int(config[5]) + 50)
        write_config_file(config)

def led_bright_down(config):
    if int(config[5]) < 55:
        #if value would be out of bounds dont do it
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[5] = str(int(config[5]) - 50)
        write_config_file(config)

def led_color_red(config):
    if config[2] == 'RED':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[2] = 'RED' 
        write_config_file(config)

def led_color_green(config):
    if config[2] == 'GREEN':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[2] = 'GREEN' 
        write_config_file(config)

def led_color_blue(config):
    if config[2] == 'BLUE':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[2] = 'BLUE' 
        write_config_file(config)

def led_color_pink(config):
    if config[2] == 'PINK':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[2] = 'PINK' 
        write_config_file(config)

def led_color_teal(config):
    if config[2] == 'TEAL':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[2] = 'TEAL' 
        write_config_file(config)

def led_color_orange(config):
    if config[2] == 'ORANGE':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[2] = 'ORANGE' 
        write_config_file(config)

def led_color_purple(config):
    if config[2] == 'PURPLE':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[2] = 'PURPLE' 
        write_config_file(config)

def led_color_yellow(config):
    if config[2] == 'YELLOW':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[2] = 'YELLOW' 
        write_config_file(config)

def led_color_grey(config):
    if config[2] == 'GREY':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[2] = 'GREY' 
        write_config_file(config)

def led_pattern_idle(config):
    if config[4] == 'IDLE':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[4] = 'IDLE' 
        write_config_file(config)

def led_pattern_wave(config):
    if config[4] == 'WAVE':
        pass
    else:
        config[-1] = str(int(config[-1]) + 1)
        config[4] = 'WAVE' 
        write_config_file(config)

def write_config_file(config):
    np.savetxt('/home/pi/LED-Project/config.txt', config[None], delimiter=' ', header='# Config file for LED controll', comments='#Power ON(1)/OFF(0); Automatic ON(1)/OFF(0); COLOR(TEXT); MODE(GAMING/MUSIC); SHOW(Idle, Wave); Intensenty(0-255); Version', fmt='%s')

def read_config_file():
    power, auto, color, mode, show, intens, version = np.genfromtxt('/home/pi/LED-Project/config.txt', dtype='str')
    return np.array([power, auto, color, mode, show, intens, version])



if __name__ == '__main__':
    

    parser = OptionParser()
    parser.add_option('-o', '--operation', type='string', dest='operation')
    (options, args) = parser.parse_args()

    
    operation = options.operation

    config = read_config_file()

    if operation == 'lsn':
        led_stripes_on(config)
    elif operation == 'lsf':
        led_stripes_off(config)
    elif operation == 'lan':
        led_automatic_on(config)
    elif operation == 'laf':
        led_automatic_off(config)
    elif operation == 'lmg':
        led_mode_gaming(config)
    elif operation == 'lmm':
        led_mode_music(config)
    elif operation == 'lmc':
        led_mode_custom(config)
    elif operation == 'lbu':
        led_bright_up(config)
    elif operation == 'lbd':
        led_bright_down(config)
    elif operation == 'lcr':
        led_color_red(config)
    elif operation == 'lcg':
        led_color_green(config)
    elif operation == 'lcb':
        led_color_blue(config)
    elif operation == 'lcp':
        led_color_pink(config)
    elif operation == 'lct':
        led_color_teal(config)
    elif operation == 'lco':
        led_color_orange(config)
    elif operation == 'lcu':
        led_color_purple(config)
    elif operation == 'lcy':
        led_color_yellow(config)
    elif operation == 'lce':
        led_color_grey(config)
    elif operation == 'lpi':
        led_pattern_idle(config)
    elif operation == 'lpw':
        led_pattern_wave(config)
    else:
        print('Wrong Option.')
        


    
   