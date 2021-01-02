
import robo 
import time as t
import random as r
import machine as m
#DEFININDO UART PARA FALAR COM PC VIA USB
uart = m.UART(0)

uart.init(114000, bits=8, parity= None, stop=1)

robozin = robo.robo()
print('robozin %i - %i', robozin.motor1, robozin.luz)

#print('robozin mot2', robozin.motor2)
#print('robozin luz' , robozin.luz.read())
saudacoes = [(0, 'oie.'), (1, 'hola.'), (2, 'hey.')]

while True:
  #print('reiniciando...')
  t.sleep(2)
  #robozin.anda()
  print(saudacoes[0])
  try:
    uart.write('Hello: ')
    #print(robozin.luz.olha())
    print('robozin luz' , robozin.luz)
  except SyntaxError:
    print('deu pau no write ou no r.adc')
  try:
    print('Lendo serial...')
    #recebido = uart.read()
    #file = open(serialTeste.txt,"r+")
    #print(recebido)
  except SyntaxError:
    print('deveria funcionar')



  



