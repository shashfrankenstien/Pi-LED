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
                        GPIO.cleanup()
                        time.sleep(0.5)
                #time.sleep(1)

def each_high((pin,gnd)):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(gnd, GPIO.OUT)
        GPIO.output(gnd, GPIO.LOW)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

def each_low((pin,gnd)):
        GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()


GPIO.setmode(GPIO.BOARD)
pins = [29, 31, 33, 35, 37, 36, 38, 40]
gnds = [7, 13, 11]
pinsRev = pins[::-1]

pin_config = [(29, 7), (29, 11), (29, 13),
                (31, 7), (31, 11), (31, 13),
                (33, 7), (33, 11), (33, 13),
                (35, 7), (35, 11), (35, 13),
                (37, 7), (37, 11), (37, 13),
                (36, 7), (36, 11), (36, 13),
                (38, 7), (38, 11), (38, 13),
                (40, 7), (40, 11), (40, 13)]
# rain(gnds, pins)

for each in pin_config:
        each_high(each)
        time.sleep(0.5)
        each_low(each)

GPIO.cleanup()
