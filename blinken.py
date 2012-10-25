import RPi.GPIO as GPIO
import threading
import time

mode = GPIO.BCM

# red = 17
# orange or yellow = 18

class Blinker():
    #TODO: modify to take 2nd pin argument in order to properly toggle between 2 pins without any hardcoding
    def __init__(self, mode, pin):
       self.pin = pin
       self.mode = mode
       GPIO.setmode(self.mode)
       GPIO.setup(self.pin, GPIO.OUT)
       GPIO.setup(18, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
 
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)

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
    def __init__(self, delay):
        self.blinker = Blinker(GPIO.BCM, 17)
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
   #         self.stoprequest.wait()
        self.blinker.cleanup()
        pass

    def stop(self):
        self.stoprequest.set()

