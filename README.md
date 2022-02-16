

# Updates from BOB
This is a forked project of PyDMX
You can find the link to the original project below
https://github.com/YoshiRi/PyDMX

I modified the code to make the system work with
* Stage APE: APE LED 86
  - There are also some items that look like this
* The generic type that looks like it
* ultra DMX Micro: this is a dmx controler that has no proper documentation
  - https://dmxking.com/usbdmx/ultradmxmicro
  - This emulates this controller [ENTTEC DMX USB Pro 512-Ch USB DMX Interface](https://www.sweetwater.com/store/detail/DMXUSBPro--enttec-dmx-usb-pro-512-ch-usb-dmx-interface?mrkgadid=3301332569&mrkgcl=28&mrkgen=gpla&mrkgbflag=0&mrkgcat=livesound&lighting&acctid=21700000001645388&dskeywordid=92700046938524260&lid=92700046938524260&ds_s_kwgid=58700005283381190&ds_s_inventory_feed_id=97700000007215323&dsproductgroupid=468822162389&product_id=DMXUSBPro&prodctry=US&prodlang=en&channel=online&storeid=&device=c&network=g&matchtype=&adpos=largenumber&locationid=9005925&creative=280136035561&targetid=pla-468822162389&campaignid=1465475237&awsearchcpc=1&gclsrc=ds&gclsrc=ds)
  - [Enttec Website link](https://www.enttec.com/product/lighting-communication-protocols/dmx512/dmx-usb-interface/)

Highly suggested you download the follwoing firmware [Pro Utility 2.2](https://dol2kh495zr52.cloudfront.net/download/dmx_usb_pro/pro_utility_setup.exe)
## What are the edits
I set the header bytes for this and the end byte. It's basically the Code from Bryan Maher but in python


## Extra resources
https://wiki.etc.cmu.edu/index.php/DMX_Board
This is the DMX code in C#. Thank you Bryan Maher


[ENTTEC DMX USB Pro 512-Ch USB DMX Interface](https://www.sweetwater.com/store/detail/DMXUSBPro--enttec-dmx-usb-pro-512-ch-usb-dmx-interface?mrkgadid=3301332569&mrkgcl=28&mrkgen=gpla&mrkgbflag=0&mrkgcat=livesound&lighting&acctid=21700000001645388&dskeywordid=92700046938524260&lid=92700046938524260&ds_s_kwgid=58700005283381190&ds_s_inventory_feed_id=97700000007215323&dsproductgroupid=468822162389&product_id=DMXUSBPro&prodctry=US&prodlang=en&channel=online&storeid=&device=c&network=g&matchtype=&adpos=largenumber&locationid=9005925&creative=280136035561&targetid=pla-468822162389&campaignid=1465475237&awsearchcpc=1&gclsrc=ds&gclsrc=ds)


[The C# project that this was edited based on](https://wiki.etc.cmu.edu/images/1/13/DMX.zip)



# PyDMX (Orignal Readme)
Python based DMX control demo program.

## Requirement
- USB-RS485 Converter
- PySerial
- wxPython (only for fader)

I used [DTECH USB-RS485 Converter](https://www.amazon.co.jp/DTECH-USB%E3%82%B7%E3%83%AA%E3%82%A2%E3%83%AB%E3%83%9D%E3%83%BC%E3%83%88%E3%82%B3%E3%83%B3%E3%83%90%E3%83%BC%E3%82%BF%E3%83%BC-RS422%E3%81%AB%E6%8E%A5%E7%B6%9A-FTDI%E3%83%81%E3%83%83%E3%83%97%E4%BB%98%E3%81%8D%E3%82%A2%E3%83%80%E3%83%97%E3%82%BF%E3%83%BC%E3%82%B1%E3%83%BC%E3%83%96%E3%83%ABWindows-Xp%E3%81%8A%E3%82%88%E3%81%B3Mac%E3%81%AB%E5%AF%BE%E5%BF%9C/dp/B076WVFXN8/ref=sr_1_1?ie=UTF8&qid=1533279683&sr=8-1&keywords=Dtech+USB+RS485).

to instal pyserial, try

```
pip install pyserial
```

for the GUI fader, wxPython is used.

```
pip install wxPython
```

# How to use

## PyDMX.py

`PyDMX.py` contains simple DMX control class.

For the instance create the connection like below:

```python
from PyDMX.py import *

dmx = PyDMX('COM3') # for Linux use '/dev/ttyUSB0' or something
```

then, you can set '255' value in the address '1' as following:

```python
dmx.set_data(1,255)
```

Finally use `send()` function to send dmx signals.

```
dmx.send()
```

### Communication option

Here shows option in the constructor.


- `Option Name` (Default Value)
  - COM (`COM8`): Comport device name.  Check it on your device manager.
  - Cnumber (`512`): DMX channels number. DMX512 protocol uses 512 channel.
  - Brate (`250000`): Baudrate. Usually do not need change.
  - Bsize (`8`): Bite size decided by DMX512 protocol.
  - StopB (`2`): Stop bit number decided by DMX512 protocol.


You can add these options like a following example.

```python
mydmx = PyDMX('/dev/ttyUSB0',Cnumber=1,Brate=9600)
```

### save and load past data

To save and load past DMX data, you can try following option.

- `Option Name` (Default Value)
  - use_prev_data (`False`): Set `True` if you want to preserve and load past DMX data.
  - preserve_data_name (`"preserved_data.txt"`): saved data file name.

## PyDMX_fader.py

`PyDMX_fader.py` contains the GUI fader class named `Controller()`.

You can just run this program as a fader.

```
python PyDMX_fader.py <fader channel number>
```

The default fader channel number is 4.

You may see following window after putting the COM port.
![](https://i.imgur.com/Z1E0KOP.png)


# Program flow

DMX is a kind of serial communication.
See Japanese explanation [here](https://qiita.com/ossyaritoori/items/53c3dd438d4232515c18).

![](https://camo.qiitausercontent.com/bd9629642e937d38c088b68cd2711a7cc5a8a4fd/687474703a2f2f7777772e74616d61746563682e636f2e6a702f74616d6164612f646d78312e676966)

You need,

- 250kbps baudrate, 1 startbit, 2 stopbit
- Break(LOW) Longer than 88us
- MAB(High) Longer than 8us
- startcode before data


# For Debugging

DMX Break length and MAB length are not rigidly defined.
You'll need to change these parameter depends on your devices.
