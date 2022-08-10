#!/usr/bin/env python


# I modified the code of Nicholas Narsing  soren121/morse.py
# https://gist.github.com/soren121/c0b7dcb905ae45d4249f
#
# This code is used with ODROID C2 on Ubuntu.
# There is no working warranty.
# You parse a string and it's converted in morse code.
#
# e.g : sudo python morse_GPIO_ODROID_C2.py "CQ CQ CQ DE F4HRB F4HRB F4HRB PSE K"
#
# it uses pin 11 and 12 as output. I had a board with two photocouplers EL 817 
# buyed in china to send dih, dah signals to my lambic double paddle MFJ-564B.
# I had to modify photocoupler board there was 3K resistors in series
# with leds of EL 817, i replaced them with a 75 Ohms resistors.
# There was also 3K ohms in series with photo transistors.
# I removed them and just made a shunt.
# The variable Dit_Time_unit have to be adapted with your RIG
# I use a chineese clone of MCHF QRP transceiver.
# I fixed the transmitted speed to 16 wpm
#
# F4HRB - Thierry Vieil  - August 10, 2022

import odroid_wiringpi as wpi
import sys, time, os
Dit_Time_unit = 0.07
DitPin = 0  # Pin connector 11
DatPin = 1  # Pin connector 12

def blink(duration):
    pin = 2
    #print(duration)
    if duration == 1 : pin=DitPin
    if duration == 3 : pin=DatPin
    wpi.digitalWrite(pin, 1)
    time.sleep(duration * Dit_Time_unit)
    wpi.digitalWrite(pin, 0)
    time.sleep(Dit_Time_unit)

morse = {
    'a': [1, 3],
    'A': [1, 3],
    'b': [3, 1, 1, 1],
    'B': [3, 1, 1, 1],
    'c': [3, 1, 3, 1],
    'C': [3, 1, 3, 1],
    'd': [3, 1, 1],
    'D': [3, 1, 1],
    'e': [1],
    'E': [1],
    'f': [1, 1, 3, 1],
    'F': [1, 1, 3, 1],
    'g': [3, 3, 1],
    'G': [3, 3, 1],
    'h': [1, 1, 1, 1],
    'H': [1, 1, 1, 1],
    'i': [1, 1],
    'I': [1, 1],
    'j': [1, 3, 3, 3],
    'J': [1, 3, 3, 3],
    'k': [3, 1, 3],
    'K': [3, 1, 3],
    'l': [1, 3, 1, 1],
    'L': [1, 3, 1, 1],
    'm': [3, 3],
    'M': [3, 3],
    'n': [3, 1],
    'N': [3, 1],
    'o': [3, 3, 3],
    'O': [3, 3, 3],
    'p': [1, 3, 3, 1],
    'P': [1, 3, 3, 1],
    'q': [3, 3, 1, 3],
    'Q': [3, 3, 1, 3],
    'r': [1, 3, 1],
    'R': [1, 3, 1],
    's': [1, 1, 1],
    'S': [1, 1, 1],
    't': [3],
    'T': [3],
    'u': [1, 1, 3],
    'U': [1, 1, 3],
    'v': [1, 1, 1, 3],
    'V': [1, 1, 1, 3],
    'w': [1, 3, 3],
    'W': [1, 3, 3],
    'x': [3, 1, 1, 3],
    'X': [3, 1, 1, 3],
    'y': [3, 1, 3, 3],
    'Y': [3, 1, 3, 3],
    'z': [3, 3, 1, 1],
    'Z': [3, 3, 1, 1],
    '0': [3, 3, 3, 3, 3],
    '1': [1, 3, 3, 3, 3],
    '2': [1, 1, 3, 3, 3],
    '3': [1, 1, 1, 3, 3],
    '4': [1, 1, 1, 1, 3],
    '5': [1, 1, 1, 1, 1],
    '6': [3, 1, 1, 1, 1],
    '7': [3, 3, 1, 1, 1],
    '8': [3, 3, 3, 1, 1],
    '9': [3, 3, 3, 1, 1],
    '?': [1, 1, 3, 3, 1, 1],
    '=': [3, 1, 1, 1, 3],
    '/': [3, 1, 1, 3, 1],
    ' ': [4],
}

def main(msg):
    wpi.wiringPiSetup()
    wpi.pinMode(0,1)
    wpi.pinMode(1,1)
    try:
        for char in msg:
            #print(char)
            if char in morse:
                for beep in morse[char]:
                    #print(beep)
                    blink(beep)
            time.sleep(2 * Dit_Time_unit)
    finally:
        cmd1 = 'gpio write ' + str(DitPin) + ' 0'
        cmd2 = 'gpio write ' + str(DatPin) + ' 0'
        os.system(cmd1)
        time.sleep(1)
        os.system(cmd2)
        time.sleep(1)
        print("Message transmitted.")


if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print("usage: morse_GPIO_ODROID_C2.py [input string]")
