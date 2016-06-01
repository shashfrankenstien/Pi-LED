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
        #GPIO.setmode(GPIO.BOARD)
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

pin_config = {0:(29, 7), 1:(29, 11), 2:(29, 13),
                3:(31, 7), 4:(31, 11), 5:(31, 13),
                6:(33, 7), 7:(33, 11), 8:(33, 13),
                9:(35, 7), 10:(35, 11), 11:(35, 13),
                12:(37, 7), 13:(37, 11), 14:(37, 13),
                15:(36, 7), 16:(36, 11), 17:(36, 13),
                18:(38, 7), 19:(38, 11), 20:(38, 13),
                21:(40, 7), 22:(40, 11), 23:(40, 13)}
# rain(gnds, pins)
while True:
	# zigzag=[0,1,2,5,4,3,6,7,8,11,10,9,12,13,14,17,16,15,18,19,20,23,22,21]
        zigzag_wide=[0,1,2,5,8,7,6,9,12,13,14,17,20,19,18,21,22,23,20,17,16,15,12,9,10,11,8,5,4,3,]
	for x in zigzag_wide:
		GPIO.setmode(GPIO.BOARD)
        	each_high(pin_config[x])
        	#each_high(pin_config[23-x])

        	time.sleep(0.1)
        	each_low(pin_config[x])
        	#each_low(pin_config[23-x])
# GPIO.cleanup()


GPIO.cleanup()
