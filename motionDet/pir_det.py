#/usr/bin/python
#

import time
import RPi.GPIO as io

io.setmode(io.BCM)

pir_pin = 18

io.setup(pir_pin, io.IN)

while True:
    if io.input(pir_pin):
	print ("PIR Alarm!")
    time.sleep(0.5)

