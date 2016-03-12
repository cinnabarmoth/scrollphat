#!/usr/bin/env python

import scrollphat
import time
import sys

msg=raw_input("Please enter your message: ")

for letter in msg:
  scrollphat.write_string(letter)
  time.sleep(0.7)
  scrollphat.clear()
