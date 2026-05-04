from machine import Pin

led = Pin("LED", Pin.OUT)
button1=Pin(0,Pin.IN,Pin.PULL_DOWN)

while True:
    if button1.value() == 1:
        led.on()
    else:
        led.off()