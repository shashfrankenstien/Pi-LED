#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def blink(i):
        GPIO.output(i, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(i, GPIO.LOW)
        return 0

def rain(gnds, pins):
        while True:
                for gnd in gnds:
                        GPIO.setmode(GPIO.BOARD)
                        GPIO.setup(gnd, GPIO.OUT)
                        GPIO.output(gnd, GPIO.LOW)
                        for pin in pins:
                                GPIO.setup(pin, GPIO.OUT)
                                GPIO.output(pin, GPIO.HIGH)
                                time.sleep(0.01)
                                GPIO.output(pin, GPIO.LOW)
                                blink(pin)
                        GPIO.cleanup()
                        time.sleep(0.5)
                #time.sleep(1)


GPIO.setmode(GPIO.BOARD)
pins = [29, 31, 33, 35, 37, 36, 38, 40]
gnds = [7, 13, 11]
pinsRev = pins[::-1]

# GPIO.setup(7, GPIO.OUT)
# GPIO.output(7, GPIO.LOW)

rain(gnds, pins)

GPIO.cleanup()
