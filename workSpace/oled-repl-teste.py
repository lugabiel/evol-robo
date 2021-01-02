from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

from fbconsole import FBConsole
import os
scr = FBConsole(oled)
os.dupterm(scr)        # redirect REPL output to OLED
help()                 # and print something
#os.dupterm(None)       # then disconnect OLED from REPL
#scr.cls()              # and clear OLED screen
