
######################
import network 
WiFi_SSID = "REDE WIFI"
WiFi_PASS = "SENHA WIFI" 

def do_connect():
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  if not wlan.isconnected():
    print('conectando à rede...')
    wlan.connect(WiFi_SSID,WiFi_PASS)
    while not wlan.isconnected():
      pass
  print('config de rede:',wlan.ifconfig())

do_connect()
#########################
from umqtt.simple import MQTTClient

SERVER = "mqtt.thingspeak.com"
client = MQTTClient("umqtt_client",SERVER)
CHANNEL_ID = "1256928"
WRITE_API_KEY = "NVTHCEC6AIBF4QDY"

topic = "channels/"+CHANNEL_ID+"/publish/"+WRITE_API_KEY

########################
import machine as m, time as t, math
import urandom as ur, neopixel

def naturais():
  num_natural=0
  while True:
    yield num_natural
    num_natural += 1

def dadoSimulado():
  print(hex(27))
  print('Hello')
  t.sleep(1)

def sendPulse(fita,ledCount,cores):
  led = 0
  colorFlag= 1
  while True:
    fita[led] = cores[colorFlag]
    fita.write()
    t.sleep(0.1)
    
    if led >= ledCount-1:
      led = 0
      colorFlag += 1
      #print(colorFlag)
      if colorFlag >= len(cores):
        colorFlag = 0
      fita[led] = cores[colorFlag]
    print('#',led)
    led += 1
 
num = naturais()
def main():
  while True:
    t.sleep(2)
    #next(num)
    payload = "field1="+str(next(num))+"&field2="+str(100*math.sin(next(num))/math.pi)
    client.connect()
    client.publish(topic,payload)
    client.disconnect()
    print(payload)
    

main()
randR = ur.getrandbits(2)
randG = ur.getrandbits(2)
randB = ur.getrandbits(2)
r,g,b = randR*2,randG*2,randB*2


vermelho = (r,0,0)
cor1     = (r,g,0)
verde    = (0,g,0)
cor2     = (0,g,b)
azul     = (0,0,b)
cor3     = (r,0,b)
preto    = (0,0,0)
branco   = (r,g,b)

cores    = [vermelho,cor1,verde,cor2,azul,cor3,preto,branco]
D4 = m.Pin(2, m.Pin.OUT)
fita = neopixel.NeoPixel(D4,144)
cor = (100,0,100)

#fita[led] = cor
sendPulse(fita,144,cores)
#fita.write()















