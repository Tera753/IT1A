from machine import Pin
from utime import sleep

start_pin = 0
end_pin = 3
pos = start_pin
ink = 1
pins=[]
running =  False
lastState = 0

for i in range(start_pin, end_pin +1):
    pins.append(Pin(i,Pin.OUT))
buzzer=Pin(4,Pin.OUT)
button=Pin(5,Pin.IN,Pin.PULL_DOWN)
   
print("Jizda zacina!!!")

while True:
    try:
        currentstav = button.value()
        if currentstav == 1 and lastState == 0:
            running = not running
        lastState = currentstav
        

        
        if running:
            pins[pos].on()
            sleep(0.2)
            pins[pos].off()
            
            pos += ink
            
            if (pos > end_pin) or (pos < start_pin):
                ink *= -1
                pos += 2*ink
                buzzer.on()
                sleep(0.1)
                buzzer.off()
            
        
    except KeyboardInterrupt:
            for pin in pins:
                pin.off()
                buzzer.off()
            print("Konec")
            break
        