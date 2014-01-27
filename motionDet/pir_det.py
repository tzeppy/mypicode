#/usr/bin/python
#

import time
import datetime
import RPi.GPIO as io

io.setmode(io.BCM)

pir_pin = 18

io.setup(pir_pin, io.IN)

while True:
    if io.input(pir_pin):
	nowstr = datetime.datetime.now().isoformat()
	print "PIR Alarm at", nowstr
	time.sleep(30.0)
    else:
        time.sleep(0.5)

