from machine import Pin
from utime import ticks_ms,ticks_diff, sleep_ms

mic = Pin(0,Pin.IN)
buzzer = Pin(1,Pin.OUT)

while True:
    try:
        buzzer.value(mic.value())
        print(mic.value())
        sleep_ms(100)
    
    except KeyboardInterrupt:
        buzzer.off()
        break
    






