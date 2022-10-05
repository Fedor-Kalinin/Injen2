import RPi.GPIO as gp
import time as t

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)
gp.setup(troyka, gp.OUT, initial = gp.HIGH)
gp.setup(comp, gp.IN)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
gp.setup(leds, gp.OUT)
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
        a = adc()
        a1 = a
        k = 250 / 8
        for d in leds:
            if a1 > k:
                gp.output(d, 1)
                a1 -= k
            else:
                gp.output(d, 0)
        print("цифровое-", a, "напряжение", end = " ")
        print("{:.3f}".format(a * 3.3 / 2 ** 8))
            
finally:
    gp.output(dac, 0)
    gp.output(troyka, 0)
    gp.output(leds, 0)
    gp.cleanup()