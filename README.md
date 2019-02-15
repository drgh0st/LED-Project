# LED-Stipe Controll
A controll script written in python which controlls LED stripes.

It currently runs on a Raspberry Pi.

## _TODO_
- [ ] write usage instructions
- [X] run on raspberry pi
- [X] write initial pattern
- [X] write gaming mode
- [X] write time circuit
- [ ] other animation
- [X] remote Controll
- [X] adjust brightness
- [ ] custom mode
- [ ] controll over hole rooms






[1]: https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/ 'Initial Instruction'

sudo apt-get update

sudo apt-get install gcc make build-essential python-dev git scons swig

sudo nano /etc/modprobe.d/snd-blacklist.conf
->blacklist snd_bcm2835

sudo nano /boot/config.txt
#dtparam=audio=on

sudo reboot

git clone https://github.com/jgarff/rpi_ws281x

cd rpi_ws281x/
sudo scons

cd python

sudo python setup.py build
sudo python setup.py install

git clone https://github.com/drgh0st/LED-Project.git