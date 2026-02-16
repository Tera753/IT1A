from machine import Pin, PWM
from utime import sleep_ms

MAX_JAS = 65535
MIN_JAS = 0
FREKVENCE = 1000

leds = []

for i in range(4):
    led = PWM(Pin(i))
    led.freq(FREKVENCE)
    led.duty_u16(MIN_JAS)
    leds.append(led)

#Wrappery
def zapni(led_obj):
    led_obj.duty_u16(MAX_JAS)

def vypni(led_obj):
    led_obj.duty_u16(MIN_JAS)

def zhasni_vse():
    for led in leds:
        vypni(led)

def zapni_pozvolna(led_obj):
    for duty in range(MIN_JAS, MAX_JAS, 1500):
        led_obj.duty_u16(duty)
        sleep_ms(20)

def vypni_pozvolna(led_obj):
    for duty in range(MAX_JAS, MIN_JAS, -1500):
        led_obj.duty_u16(duty)
        sleep_ms(20)

def hadR():
    zhasni_vse()
    for led in leds:
        zapni(led)
        sleep_ms(200)
        vypni(led)

def hadL():
    zhasni_vse()
    for led in reversed(leds):
        led.on()
        sleep_ms(200)
        led.off()
        
        
def breath():        
    for duty in range(MIN_JAS, MAX_JAS, 1500):
        for led in leds:
            led.duty_u16(duty)
        sleep_ms(50)
    for duty in range(MAX_JAS, MIN_JAS,-1500):
        for led in leds:
            led.duty_u16(duty)
        sleep_ms(50)


def poz_breath():
    for led in leds:
        zapni_pozvolna(led)
    for led in leds:
        vypni_pozvolna(led)
        vypni(led)

        
        

        

    
    
while True:
    try:
        poz_breath() 
    except KeyboardInterrupt:
        zhasni_vse()
        print("Exit")
        break
