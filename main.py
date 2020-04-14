from robo import robo
import random



robozin = robo()

print(robozin)
print(robozin.luz)
print(robozin.mov)

luzMax = 0.8


while True:
    robozin.olha()
    robozin.anda()
    robozin.para()
    
    
