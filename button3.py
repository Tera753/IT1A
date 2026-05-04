from machine import Pin
from utime import sleep_ms

led = Pin("LED", Pin.IN)
button1=Pin(0,Pin.IN,Pin.PULL_DOWN)

lastState = 0

while True:
    currentState = button1.value()
    
    if currentState == 1 and lastState == 0:
        led.toggle()
        sleep_ms(50)
    lastState = currentState