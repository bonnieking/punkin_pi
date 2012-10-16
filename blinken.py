import RPi.GPIO as GPIO
import threading
import time

mode = GPIO.BCM

# red = 18
# orange = 17


class Blinker():
    def __init__(self, mode, pin):
       self.pin = pin
       self.mode = mode
       GPIO.setmode(self.mode)
       GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
 
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def blink(self, delay):
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

class BlinkRun(threading.Thread):
    def __init__(self, delay, blinker):
        self.blinker = blinker
        self.delay = delay        
        self.stoprequest = threading.Event()
        self.terminated = False

    def changedelay(self, units, increment=0.01):
        # increase or decrease delay. Default increment 0.1secs
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
            self.blinker.blink(self.delay)
        self.terminated = True
        self.blinker.cleanup()

    def stop(self):
        self.stopme = True
        while self.terminated == False:
            time.sleep(0.01)
        self.blinker.reset()

    def join(self, timeout=None):
        self.stoprequest.set()
        super(BlinkRun, self).join(timeout)
