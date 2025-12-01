from machine import Pin
from utime import sleep

pin0= Pin(0,Pin.OUT)
pin1= Pin(1,Pin.OUT)
pin2= Pin(2,Pin.OUT)

while True:

    pin2.on()
    sleep(3)
    pin1.on()
    sleep(1)
    pin2.off()
    pin1.off()
    pin0.on()
    sleep(5)
    pin0.off()
    