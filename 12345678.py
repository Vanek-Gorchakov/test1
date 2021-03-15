import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
numbers = [10, 9, 11, 5, 6, 13, 19, 26]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
for n in numbers:
    GPIO.setup(n, GPIO.OUT)
for i in range(8):
    GPIO.output(numbers[i], 0)
for n in leds:
    GPIO.setup(n, GPIO.OUT)
def lightUp(ledNumber, period):
    GPIO.output(leds[ledNumber], 1)
    time.sleep(period)
    GPIO.output(leds[ledNumber], 0)
def blink (ledNumber, blinkCount, blinkPeriod):
    while blinkCount:
        blinkCount -= 1
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)
def runningLight(count, period):
    for i in range(count):
        for j in range(8):
            lightUp(j, period)
def DarkUp(ledNumber, period):
    GPIO.output(leds[ledNumber], 0)
    time.sleep(period)
    GPIO.output(leds, 1)
def runningDark(count, period):
    GPIO.output(leds, 1)
    for i in range(count):
        for j in range(8):
            DarkUp(j, period)
    

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