
import machine as m, neopixel, time as t, math



class LED(object):
  #   
  #
  #
  def __init__(self):
    print('new led available')
    self.fita = m.Pin(2, m.Pin.OUT)
    self.ledCount = 144
    self.cor = (100, 0, 100)
  def sendPulse(self, fita, ledCount, cor):
    led = 0
    while True:
      fita[led-1]   = (0,0,0)
      fita[led] = cor
      t.sleep(0.00005)
      fita.write()
      if led == ledCount-1:
        fita[led]   = (0,0,0)
        led = 0
        self.sendPulse(fita, ledCount, cor)
      print(led)
      led += 1

D4 = m.Pin(2, m.Pin.OUT)
fita = neopixel.NeoPixel(D4,144)
roxo = (100,0,100)


L  = LED()
L.sendPulse(fita,144, roxo)


#fita.write()



