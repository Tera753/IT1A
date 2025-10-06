from machine import Pin
from utime import sleep


pin0= Pin(0,Pin.OUT)
pin1= Pin(1,Pin.OUT)
pin2= Pin(2,Pin.OUT)
pin3= Pin(3,Pin.OUT)

print("zaciname")
while True:
    try:
        pin0.toggle()
        sleep(1)
        pin0.off()

        pin1.toggle()
        sleep(2)
        pin1.off()

        pin2.toggle()
        sleep(3)
        pin2.off()

        pin3.toggle()
        sleep(4)
        pin3.off()
        
    except KeyboardInterrupt:
        print("konec")

        break

# kratší zpusob
from machine import Pin
from utime import sleep

start_pin = 0
end_pin = 3
position = start_pin
ink = 1
pins=[]

for i in range(start_pin, end_pin +1):
    pins.append(Pin(i, Pin.OUT))

while True:
    try:
        pins[position].on()
        sleep(0.2)
        pins[position].off()
        position += ink

        if(position > end_pin) or (position < start_pin):
            ink*= -1
            position+= 2*ink
    except KeyboardInterrupt:
        for pin in pins:
            pin.off()