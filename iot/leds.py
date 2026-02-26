#  Nmae : Daniel nduati
# Date : 23/02/2026
# program to blink led
from machine import Pin
import time
red_led = Pin(28, Pin.OUT)
yellow_led = Pin(27,Pin.OUT)
while True:
    red_led.on()
    yellow_led.off()
    time.sleep(0.4) # Wait for USB to become ready
    red_led.off()
    yellow_led.on()
    time.sleep(0.6)
    print("ERROR 404")
