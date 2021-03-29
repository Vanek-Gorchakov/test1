import numpy as np
import matplotlib.pyplot as plt
from time import sleep


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
DAC = [10,9,11,5,6,13,19,26]                              
leds = [24,25,8,7,12,16,20,21]                                                                                                                                                                     
GPIO.setup(DAC, GPIO.OUT)
def num2dac(decNumber):
    return list(reversed([0]*(8-len(list(bin(decNumber))[2:])) + list(bin(decNumber))[2:]))
def lightNumber(number):
    global DAC
    GPIO.output(DAC, 0)
    leds = num2dac(number)
    for i in range(len(DAC)):
        if int(leds[i]):
            GPIO.output(DAC[i], 1)
print('Введите время работы')
t = int(input())
print('Введите частоту')
ot = 1/ int(input())
print('Введите частоту дискретизации')
dt = 1 / int(input())



time = np.arange(0, t, dt)
for i in range(len(time)):
    time[i] = time[i] * 2 * 3,14 / ot
amplitude = np.sin(time)
for i in range(len(amplitude)):
    amplitude[i] = round((amplitude[i] + 1) / 2 * 255)
time1 = np.arange(0, t ,dt)
r = list(amplitude)

for i in r:
    lightNumber(int(i))
    sleep(ot)
    GPIO.output(DAC, 0)
