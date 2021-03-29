import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
DAC = [10,9,11,5,6,13,19,26]                              
leds = [24,25,8,7,12,16,20,21]                                                                                                                                                                     
GPIO.setup(DAC, GPIO.OUT)
def num2dac(decNumber):
    return list(reversed([0]*(8-len(list(bin(decNumber))[2:])) + list(bin(decNumber))[2:]))
def lightNumber(number):
    global D
    GPIO.output(DAC, 0)
    leds = num2dac(number)
    for i in range(len(DAC)):
        if int(leds[i]):
            GPIO.output(DAC[i], 1)

while True:
    print('Введите число (-1 для выхода)')
    s = input()
    print(s.isdigit(), s != '-1')
    if s.isdigit() == False and s != '-1':
        print('введите число')
        continue
    if int(s) < -1 or int(s) > 255:
        print ("введите число в диапазоне от -1 до 255")
        continue
    if s =='-1':
        print('Выход')
        break
    lightNumber(int(s))

GPIO.cleanup()