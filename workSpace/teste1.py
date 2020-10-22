import machine as m
import time as t

#---WEMOS D1 PIN <- ESP8266 PIN---#
D0 = m.Pin(16,m.Pin.OUT)
D5 = m.Pin(14,m.Pin.OUT)
D1 = m.Pin(5,m.Pin.OUT)
led = m.Pin(2, m.Pin.OUT)
periodo = 0.9

pwmD1 = m.PWM(D1) 
pwmD5 = m.PWM(D5)

pwmD1.freq(60)
pwmD1.duty(1024) 
pwmD5.freq(60)
pwmD5.duty(1024) 

pwmVel_d1 = 256
pwmVel_d5 = 512



while True:
  D0.off()
  led.on()
  pwmD5.duty(pwmVel_d5)
  pwmD1.duty(pwmVel_d1*8)  
  t.sleep(periodo)
  D0.on()
  led.off()
  pwmD5.duty(pwmVel_d5*2)
  pwmD1.duty(pwmVel_d1*0)
  t.sleep(periodo*2)
  


