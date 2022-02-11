from PyDMX import *

if __name__ == '__main__':
    dmx = PyDMX('COM5') # for Linux use '/dev/ttyUSB0' or something
    # This is the Strobe, needs to be set to 255 so the light stays ons
    dmx.set_data(1,255)
    # This is intensity
    dmx.set_data(2,255)
    # Red Channel
    dmx.set_data(3,0)
    # Green Controller
    dmx.set_data(4,0) 
    # Blue Controller
    dmx.set_data(5,0)
    # Don't know
    dmx.set_data(6,255)
    # Don't know
    dmx.set_data(7,0)
    dmx.send()
