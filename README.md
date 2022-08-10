morse_ODROID_C2
Python script to command lambic double paddle on a HAM transceiver

I modified the code of Nicholas Narsing  soren121/morse.py
https://gist.github.com/soren121/c0b7dcb905ae45d4249f

This code is used with ODROID C2 on Ubuntu.
There is no working warranty.
You parse a string and it's converted in morse code.

 e.g : sudo python morse_GPIO_ODROID_C2.py "CQ CQ CQ DE F4HRB F4HRB F4HRB PSE K"

it uses pin 11 and 12 as output. I had a board with two photocouplers EL 817 
buyed in china to send dih, dah signals to my lambic double paddle MFJ-564B.
I had to modify photocoupler board there was 3K resistors in series
with leds of EL 817, i replaced them with a 75 Ohms resistors.
There was also 3K ohms in series with photo transistors.
I removed them and just made a shunt.
The variable Dit_Time_unit have to be adapted with your RIG
I use a chineese clone of MCHF QRP transceiver.
I fixed the transmitted speed to 16 wpm
