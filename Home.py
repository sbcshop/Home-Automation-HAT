#!/usr/bin/python

# Library for Home Automation HAT
# Developed by: SB Components
# Author: Ankur
# Project: PiRelay
# Python: 3.4.2

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


class Relay:
    """Class to handle Relays
    Arguments:
    relay = string Relay label (i.e. "RELAY1", "RELAY2", "RELAY3", "RELAY4",
    "RELAY5", "RELAY6", "RELAY7", "RELAY8")
    """
    relaypins = {
        "RELAY1": 35, "RELAY2": 33, "RELAY3": 23, "RELAY4": 29,
        "RELAY5": 31, "RELAY6": 33, "RELAY7": 35, "RELAY8": 37
                 }

    def __init__(self, relay):
        self.pin = self.relaypins[relay]
        self.relay = relay
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        print(self.relay + " - ON")
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        print(self.relay + " - OFF")
        GPIO.output(self.pin, GPIO.LOW)
