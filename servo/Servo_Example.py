#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import sys

if len(sys.argv) != 2:
  print "usage: %prog <channel>".replace("%prog", sys.argv[0])
  sys.exit(2)

SERVO_LOC = int(sys.argv[1])

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096


def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
while (True):
  # Change speed of continuous servo on channel O
  pwm.setPWM(SERVO_LOC, 0, servoMin)
  time.sleep(1)
  pwm.setPWM(SERVO_LOC, 0, servoMax)
  time.sleep(1)



