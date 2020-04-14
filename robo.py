import random

class robo(object):
    '''
    esta eh a classe robo, entidade composta por:
    luz - corresponde a intensidade luminosa momentanea
          na região que o robo ocupou recentemente.
    mov - representa o par de comandos discretos capaz
          acionar os motores do robo.
    ''' 

    def __init__(self):
        
        self.luz = 0.0
        self.mov = [0,0]

    def initRobo(self):
        self.luminosidade = pinSensorLuz
        self.mov = [random.randint(-1,1),random.randint(-1,1)]
            
