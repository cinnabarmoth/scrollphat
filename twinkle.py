#!/usr/bin/env python

#leds on scrollphat light up in a random sequence giving a twinkling effect

import scrollphat
import time
import random
import sys

def light(pause):
        xValue = random.randrange(10)
        yValue = random.randrange(5)
        scrollphat.set_pixel(xValue, yValue, 1)
        scrollphat.update()
        time.sleep(pause)

def off(pause):
        xValue = random.randrange(10)
        yValue = random.randrange(5)
        scrollphat.set_pixel(xValue, yValue, 0)
        scrollphat.update()
        time.sleep(pause)

while(True):
        try:
                pause_time = 0.05
                light(pause_time)
                off(pause_time)
        except KeyboardInterrupt:
                scrollphat.clear()
                sys.exit(-1)
