
# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

# ESP8266 Pin assignment
#i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('..................', 0, 0)
oled.text('................:)', 0, 10)
oled.text('..............:)..', 0, 20)
        
i = 0

while True:
  if i > 50:
    i = 0
  oled.show()
  itext =  "^~^~str(i)~^~^" 
  oled.text(itext, 0, 30)
  i += 1

