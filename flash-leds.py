#!/usr/bin/env python

#switches all leds on at once and keeps them on for 1 second

import scrollphat
import time

for x in range(11):
  for y in range(5):
    scrollphat.set_pixel(x,y,1)
    scrollphat.update()
time.sleep(1)

#switches all leds off again
for x in range(11):
  for y in range(5):
    scrollphat.set_pixel(x,y,0)
    scrollphat.update();
    
