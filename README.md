import RPi.GPIO as GPIO
import time
numbers = [10, 9, 11, 5, 6, 13, 19, 26]
leds = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(16,GPIO.IN)

def dBTL(dN):
    bdN = bin(dN)
    dddN = bdN[2:15:1]
    N = dddN.zfill(8)
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        a[i] = int(N[i])
    return a

   
def lightNumber(number):
    b = dBTL(number)
    for i in range(8):
        GPIO.output(leds[7 - i], b[i])
def skript1(a):
    x = dBTL(a)
    for i in range(8):
        if x[i] == 1:
            GPIO.setup(leds[i], GPIO.OUT)
            GPIO.output(leds[i], 1)


GPIO.output(17,1)
while True:
    print('Enter value (-1 t exit) > ')
    n = int(input())
    volts = round(n*3.3/255, 2)
    if n == -1:
        for i in leds:
            GPIO.setup(i,GPIO.OUT)
            GPIO.output(i,0)
    else:
        print(n, '=' , volts, 'V' )
        for i in leds:
            GPIO.setup(i,GPIO.OUT)
            GPIO.output(i,0)
            skript1(n)

GPIO.clenup()
