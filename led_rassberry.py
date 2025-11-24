from machine import Pin
from utime import sleep

pina= Pin(0,Pin.OUT)
pinb= Pin(1,Pin.OUT)
pinc= Pin(2,Pin.OUT)
pind= Pin(3,Pin.OUT)


while True:
        pina.toggle()
        sleep(0.5)
        pina.off()
        
        pinb.toggle()
        sleep(0.5)
        pinb.off()
        
        pinc.toggle()
        sleep(0.5)
        pinc.off()
        
        pind.toggle()
        sleep(0.5)
        pind.off()