#!/usr/bin/env python

from ctypes import *
import sys
import random
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
        val = interfaceKit.getSensorvalue(0)
        print val
        time.sleep(0.5)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)

try:
    interfaceKit.closePhidget()
except PhidgetException as e:
    exit(1)

exit(0)
