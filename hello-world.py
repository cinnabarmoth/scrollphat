#!/usr/bin/env python

import scrollphat
import time
import sys

scrollphat.write_string("Hello, World");

while True:
  try:
      scrollphat.scroll()
      time.sleep(0.3)
    except KeyboardInterrupt:
    scrollphat.clear()
    sys.exit(-1)
      
