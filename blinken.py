import RPi.GPIO as GPIO
import threading
import time

mode = GPIO.BCM

red = 18
orange = 17


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

class BlinkRun(threading.Thread):
    def __init__(self, pin, delay):
        self.blinker = Blinker(mode, pin)
        self.delay = delay        
        self.stopme = False
        self.terminated = False

    def start(self):
        self.thread = threading.Thread(None, self.run, None, (), {})
        self.thread.start()

    def run(self):
        while self.stopme == False:
            self.blinker.blink(self.delay)
        self.terminated = True

    def stop(self):
        self.stopme = True
        while self.terminated == False:
            time.sleep(0.01)

     
