from machine import Pin, PWM
from utime import sleep_ms

#----------------------------Inicializační funkce-----------------------------
leds = []

for i in range(4):
    leds.append(Pin(i, Pin.OUT))

def zhasni():
    for led in leds:
        led.off()

#-----------------------------Animační funkce----------------------------------
def hadR():
    zhasni()
    for led in leds:
        led.on()
        sleep_ms(200)
        led.off()

def hadL():
    zhasni()
    for led in reversed(leds):
        led.on()
        sleep_ms(200)
        led.off()

def leftRight():
    hadL()
    hadR()

def blik():
    zhasni()
    for led in leds:
        led.on()
    sleep_ms(50)
    for led in leds:
        led.off()
    sleep_ms(50)

def blik_ob():
    zhasni()
    for j in range(2):
        for i, led in enumerate(leds):
            if i % 2 == 0:
                led.on()
        sleep_ms(100)
        zhasni()
        sleep_ms(100)

    for j in range(2):
        for i, led in enumerate(leds):
            if i % 2 != 0:
                led.on()
        sleep_ms(100)
        zhasni()
        sleep_ms(100)      




#----------------------------main část pro provádění a spouštění-----------------------------------
        
while True:
    try:
        hadL() 
        breath()   
        hadR()
    except KeyboardInterrupt:
        zhasni()
        print("Exit")
        break