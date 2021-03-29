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


def repetitionsNumber(a):
    for i in range(a):
        for j in range(256, -1, -1):
            lightNumber(j)
s = int(input('Введите число '))
repetitionsNumber(s)
GPIO.cleanup()