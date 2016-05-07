import RPi.GPIO as GPIO
import time

def blink(i):
        GPIO.output(i, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(i, GPIO.LOW)
        return 0

GPIO.setmode(GPIO.BOARD)
pins = [29, 31, 33, 35, 37, 36, 38, 40]
pinsRev = pins[::-1]
ex=[0,1,2,3,4,5,6,7]
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)
while True:
        for x in ex:
                GPIO.setup(pins[x], GPIO.OUT)
                GPIO.output(pins[x], GPIO.HIGH)
                time.sleep(0.01)
                GPIO.output(pins[x], GPIO.LOW)
        time.sleep(1)
GPIO.cleanup()
