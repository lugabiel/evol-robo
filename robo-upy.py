import machine as m
import random

# DEFINITIONS---WEMOS_D1 PIN <- ESP8266 PIN---#
D0 = m.Pin(16,m.Pin.OUT)
D5 = m.Pin(14,m.Pin.OUT)
D2 = m.Pin(4,m.Pin.IN)
D1 = m.Pin(5,m.Pin.OUT)
led = m.Pin(2, m.Pin.OUT)



class robo(object):
  '''
    esta eh a classe robo - entidade composta por:
    luz - corresponde a intensidade luminosa momentanea
          na região que o robo ocupou recentemente.
    mov - representa o par de comandos discretos capaz
          acionar os motores do robo.
    
  ''' 
  def motorInit(self, pin, duty):
    # Definindo frenquecia do pwm para motor
    self.motor.freq(60)
    # Definindo dutycicle (% do tempo ligado) do motor
    self.motor.duty(duty)
    
  def __init__(self):
    # Definindo Sensor de Luminosidade
    self.luz = m.ADC(0)
    # Definindos motores do robo
    self.motor1 = m.PWM(D1) 
    self.motor2 = m.PWM(D5)  
  
  def anda(self):
    # Ligando motores
    self.motorInit(self.motor1, 1024)
    self.motorInit(self.motor2, 1024)
    print('andando...')
    
  def para(self):
    # Desligando motores
    self.motorInit(self.motor1, 0)
    self.motorInit(self.motor2, 0)
    print('parando')
    
  def olha(self):
    print('(entre 0 e 1024) a luz aqui eh --', self.luz )
