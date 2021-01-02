########################################
# COPIE ESTE CODIGO E COLOQUE NO MAIN.PY 
#import machine as m, time as t
#from LED import LED as L
#roxo    = (100,0,100)
#amarelo = (100,100,0)
#L.sendPulse(amarelo)
########################################

class LED(object):
  

  # classe LED que define entidade 
  # de leds enderecaveis
  def __init__(self,corInput,ledCountInput):
    print('new led available')
    self.ledCount = 144
    self.ledCount = ledCountInput
    self.fita = neopixel.NeoPixel(m.Pin(2, m.Pin.OUT),self.ledCount)
    self.cor = corInput
  def sendPulse(self):
    led = 0
    while True:
      self.fita[led-1]   = (0,0,0)
      self.fita[led] = self.cor
      t.sleep(0.00005)
      self.fita.write()
      if led == self.ledCount-1:
        self.fita[led]   = (0,0,0)
        self.cor += (0,150,0)
        led = 0
      #print(led)
      led += 1

