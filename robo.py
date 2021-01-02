import random

class robo(object):
    mov = [0,0]
    luz = 0.0
    '''
    esta eh a classe robo - entidade composta por:
    luz - corresponde a intensidade luminosa momentanea
          na região que o robo ocupou recentemente.
    mov - representa o par de comandos discretos capaz
          acionar os motores do robo.

    '''
    def __init__(self):

        self.__luz = 0.0      #TODO: D2 = m.Pin(4,m.Pin.IN) -- machine.adc()
        self.mov = [0,0]

    def anda(self):
        self.mov = [random.randint(-1,1),random.randint(-1,1)]
        print('andando...', self.mov)

    def para(self):
        self.mov = [0,0]
        print('parando...')

    def olha(self):
        self.luz = random.uniform(0,1)
        print ('a luz aqui eh -- ',self.luz)
