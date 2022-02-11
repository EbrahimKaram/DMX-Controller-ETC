from DMXEnttecPro import Controller

if __name__ == '__main__':
    dmx = Controller('COM5') 
    dmx.set_channel(1, 100)  # Sets DMX channel 1 to max 255
    dmx.submit()  # Sends the update to the controller
