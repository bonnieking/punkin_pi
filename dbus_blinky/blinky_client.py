#/usr/bin/python
import dbus
import threading

class BlinkRun(threading.Thread):
    def __init__(self, delay, pin):
        bus = dbus.SystemBus()
        self.pin = pin
        self.blinkyservice = bus.get_object('com.bonnielking.BlinkyPi', '/com/bonnielking/BlinkyPi/17')
        self.delay = delay
        self.stopme = False
        self.terminated = False

    def changedelay(self, units, increment=0.01):
    
        if self.delay + (units * increment) < 0:
            self.delay = 0 
        else:
            self.delay = self.delay + (units * increment)
            print "new delay is %s" %self.delay

    def delayup(self, increment=0.01):
        self.delay = self.delay + abs(increment)
        print "new delay is %s" %self.delay

    def delaydown(self, increment=0.01):
        if self.delay - abs(increment) < 0:
            self.delay = 0 
        else:
            self.delay = self.delay - abs(increment)
        print "new delay is %s" %self.delay

    def start(self):
        self.thread = threading.Thread(None, self.run, None, (), {}) 
        self.thread.start()

    def run(self):
        while self.stopme == False:
            self.blinkyservice.get_dbus_method('on', dbus_interface='com.bonnielking.BlinkyPi')()
        self.terminated = True

    def stop(self):
        self.stopme = True
        while self.terminated == False:
            time.sleep(0.01)
        self.blinkyservice.reset()



bus = dbus.SystemBus()
blinkyservice = bus.get_object('com.bonnielking.BlinkyPi', '/com/bonnielking/BlinkyPi/17')
blink = blinkyservice.get_dbus_method('on', 'com.bonnielking.BlinkyPi')
#print blink()

