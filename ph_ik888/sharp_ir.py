#!/usr/bin/env python

from ctypes import *
import sys
import random
import time
#Phidget specific imports
from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import InterfaceKit

try:
    interfaceKit = InterfaceKit()
except RuntimeError as e:
    print("Runtime Exception: %s" % e.details)
    print("Exiting....")
    exit(1)

try:
    interfaceKit.openPhidget()
    interfaceKit.waitForAttach(10000)
    while True:
        val = interfaceKit.getSensorValue(0)
	if val >= 80 and val <= 490:
		dist = 9462.0/(val - 16.92)    # in cm
	        print "%.1f cm" % dist
        time.sleep(0.1)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)

try:
    interfaceKit.closePhidget()
except PhidgetException as e:
    exit(1)

exit(0)
