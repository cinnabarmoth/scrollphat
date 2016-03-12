#!/usr/bin/env python

"""lights a single led. The function set_pixel() takes 3 arguments - x position (in a range 0-10), y position (range 0-4) and off/on (0/1). The position of an led is given top-to-bottom, left-to-right with the scrollphat positioned so that 'scroll pHAT' is along the bottom edge and 'PIMORONI.COM' runs along the right-hand short edge."""

import scrollphat

#sets a single pixel to 'on' - in this case it is the pixel in the second from left column in the middle row 
scrollphat.set_pixel(1,2,0)
scrollphat.update();
