import RPi.GPIO as GPIO
import threading
import time

mode = GPIO.BCM

# red = 17
# orange or yellow = 18

class Blinker():
    #TODO: modify to take 2nd pin argument in order to properly toggle between 2 pins without any hardcoding
    def __init__(self, mode, pin1, pin2):
       self.pin1 = pin1
       self.pin2 = pin2
       self.mode = mode
       GPIO.setmode(self.mode)
       GPIO.setup(self.pin1, GPIO.OUT)
       GPIO.setup(self.pin2, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)
 
    def off(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)

    def blink(self, delay):
        self.on()
        time.sleep(delay)
        self.off()
        time.sleep(delay)

    def cleanup(self):
        # this is the default state of the pins
        GPIO.setup(self.pin1, GPIO.IN, GPIO.PUD_OFF)
        GPIO.setup(self.pin2, GPIO.IN, GPIO.PUD_OFF)

    def reset(self):
        self.cleanup()
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)

class BlinkRun(threading.Thread):
    def __init__(self, delay):
        self.blinker = Blinker(GPIO.BCM, 17, 18)
        self.delay = delay 
        self.stoprequest = threading.Event()
        self.stoprequest.clear()         
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
        while not self.stoprequest.isSet():
            self.blinker.blink(self.delay)
        self.blinker.cleanup()
        pass

    def stop(self):
        self.stoprequest.set()

