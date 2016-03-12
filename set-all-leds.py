#!/usr/bin/env python

#switches all led on at once

for x in range(11):
  for y in range(5):
    scrollphat.set_pixel(x,y,1)
    scrollphat.update();
