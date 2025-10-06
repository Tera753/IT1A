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
