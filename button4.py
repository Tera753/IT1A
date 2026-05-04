from machine import Pin
from utime import sleep_ms

btn1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
btn4 = Pin(3, Pin.IN, Pin.PULL_DOWN)
led = Pin("LED", Pin.OUT)

lastState = 0

while True:
    if btn1.value() == 1 and btn4.value() == 1:
        print("Kombinace stisknuta")
        sleep_ms(50)
        while btn1.value() == 1 and btn4.value() == 1:
            pass