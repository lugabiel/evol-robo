import machine as m, neopixel, time
'''
def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

'''
D0 = m.Pin(16,m.Pin.OUT)
led = m.Pin(2, m.Pin.OUT)

# quantidade de pixels 
pixelBlock = 144 

fita = neopixel.NeoPixel(D0,pixelBlock)
aux = 10
zero = (0,0,0)
fita[0] = (100,0,0)
fita[1] = (0,0,100)
fita[2] = zero
fita[3] = (0,100,0)
#fita.write()
'''
fita[3] = (155,100,aux)
fita[8] = (0,255,0)
fita[10] = (100,155,aux)

while True:
  if aux > 256:
    aux = 0
  fita.write()
  aux += 1
  led.on()
  t.sleep(2)
  led.off()
'''
