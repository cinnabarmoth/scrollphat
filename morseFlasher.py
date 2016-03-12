#!/usr/bin/env python

"""asks user to enter a message and displays it in the terminal window converted into Morse code. The user is then prompted to enter the message again (or a new message) which is displayed using the LED panel to flash the dots and dashes"""

import scrollphat
import time

#incomplete dictionary for Morse code 
CODE = {' ': '_', 'A': '.-', 'B': '-...', 'c': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}

#switches all leds on
def switchon():
        for x in range(11):
                for y in range(5):
                        scrollphat.set_brightness(4)
                        scrollphat.set_pixel(x,y,1)
                        scrollphat.update();


#1 second pause
def pause():
        time.sleep(0.6);


#switches all leds off
def switchoff():
        for x in range(11):
                for y in range(5):
                        scrollphat.set_pixel(x,y,0)
                        scrollphat.update();
def dot():
        switchon()
        time.sleep(0.3)
        switchoff()
        time.sleep(0.3);

def dash():
        switchon()
        time.sleep(0.6)
        switchoff()
        time.sleep(0.3);

def convertToMorse(msg):
        msg = msg.upper()
        encodedMsg = ""
        for character in msg:
                encodedMsg += CODE[character] + " "
        return encodedMsg

msg = raw_input("Enter message: ")
encodedMsg = convertToMorse(msg)
print(encodedMsg)

def encodeToWords(msg):
        encodedMsg = convertToMorse(msg)
        for character in encodedMsg:
                if character == '.':
                        dot()
                elif character == '-':
                        dash()
                elif character == ' ':
                        pause()
                elif character == '_':
                        pause()

msg = raw_input("Enter message: ")
encodeToWords(msg)

