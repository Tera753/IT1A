from machine import Pin
from utime import sleep, ticks_ms

start_pin=0
end_pin=3
pos=start_pin
pins=[]
ink=1
laststate=0
lastchange = ticks_ms()

for i in range(start_pin, end_pin +1):
    pins.append(Pin(i,Pin.OUT))
button1=Pin(12,Pin.IN,Pin.PULL_DOWN)
button2=Pin(13,Pin.IN,Pin.PULL_DOWN)
button4=Pin(14,Pin.IN,Pin.PULL_DOWN)

print("zaciname")
while True:
    try:
        if (pos > end_pin):
                ink *= -1
                pos += 2*ink
                button1.on()
                sleep(0.5)
                button1.off()
                
        if (pos > end_pin) or (pos < start_pin):
                ink *= -1
                pos += 2*ink
                button2.on()
                sleep(0.5)
                button2.off()
                         
        if (pos < end_pin):
                ink *= -1
                pos += 2*ink
                button4.on()
                sleep(0.5)
                button4.off()
                
           
    except KeyboardInterrupt:
        for pin in pins:
                pin.off()
                button2.off()
                print("Konec")
    break
