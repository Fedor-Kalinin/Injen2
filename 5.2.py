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
    arr = [1, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        arr[i] = 1
        gp.output(dac, arr)
        t.sleep(0.005)
        compValue = gp.input(comp)
        if compValue == 0:
            arr[i] = 0
    return 128 * arr[0] + 64 * arr[1] + 32 * arr[2] + 16 * arr[3] + 8 * arr[4] + 4 * arr[5] + 2 * arr[6] + arr[7]

try:
    while True:
        k = adc()
        if k != 0:
            print(k, int(3.3 * k / 256 * 100) / 100, 'v')

            
finally:
    gp.output(dac, gp.LOW)
    gp.cleanup(dac)