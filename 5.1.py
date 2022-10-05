import RPi.GPIO as gp
import time as t

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)
gp.setup(troyka, gp.OUT, initial = gp.HIGH)
gp.setup(comp, gp.IN)

def dec2bin(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def adc():
    for i  in range(256):
        gp.output(dac, dec2bin(i))
        t.sleep(0.005)
        compValue = gp.input(comp)
        if compValue == 0:
            return i

try:
    while True:
        i = adc()
        if i != 0:
            print(i, int(3.3 * i / 256 * 100) / 100, 'v')

            
finally:
    gp.output(dac, gp.LOW)
    gp.cleanup(dac)