#!/usr/bin/python
import RPi.GPIO as GPIO
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import gobject
import time
import threading

gobject.threads_init()

from dbus import glib
glib.init_threads()

class Blinker():
    def __init__(self, pin, mode):
       self.pin = pin
       self.mode = mode
       GPIO.setmode(self.mode)
       GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def blink(self, delay):
        # can't send floats over dbus?
        delay = float(delay) / 1000
        self.on()
        time.sleep(delay)
        self.off()
        time.sleep(delay)

    def cleanup(self):
        # this is the default state of the pin
        GPIO.setup(self.pin, GPIO.IN, GPIO.PUD_OFF)

    def reset(self):
        self.cleanup()
        GPIO.setup(self.pin, GPIO.OUT)

class BlinkyDBUSService(dbus.service.Object):
    def __init__(self, pin, mode):
        self.pin = pin
        self.blinker = Blinker(pin, GPIO.BCM)
        bus_name = dbus.service.BusName('com.bonnielking.BlinkyPi', bus=dbus.SystemBus())
        dbus.service.Object.__init__(self, bus_name, '/com/bonnielking/BlinkyPi'+str(self.pin))

    @dbus.service.method('com.bonnielking.BlinkyPi')
    def on(self):
        print "on"
        self.blinker.on()

    @dbus.service.method('com.bonnielking.BlinkyPi')
    def off(self):
        print "off"
        self.blinker.off()
        return "%s off" %self.pin

    @dbus.service.method('com.bonnielking.BlinkyPi')
    def blink(self, delay):
        print "blink"
        self.blinker.blink(delay)   

DBusGMainLoop(set_as_default=True)
delay = 1
myservice = BlinkyDBUSService(17, GPIO.BCM)
myservice = BlinkyDBUSService(18, GPIO.BCM)
loop = gobject.MainLoop()
loop.run()

