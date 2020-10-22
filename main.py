from robo import robo
import random
import time
robozin = robo()

def printDados():
    #print(robozin)
    print(robozin.luz)
    print(robozin.mov)

luzMax = 0.8


while True:

    time.sleep(2)
    if (robozin.olha()>0.4):
        robozin.anda()
    else:
        robozin.para()
    printDados()
    
