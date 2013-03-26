#!/usr/bin/python

import wiringpi
import time
from random import choice

pins = [1, 2, 3]
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
states = [io.HIGH, io.LOW]

def setup():
    for pin in pins:
        io.pinMode(pin, io.OUTPUT)
        io.digitalWrite(pin, io.LOW)

def loop():
    while True:
        for pin in pins:
            io.digitalWrite(pin, choice(states))
        time.sleep(10)

setup()
loop()
