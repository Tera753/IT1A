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

#----------------------------PWM animace----------------------------
def breath():
    pwm_leds = []
    for led in leds:
            pwm_led = PWM(led)
            pwm_led.freq(1000)
            pwm_led.duty_u16(0)
            pwm_leds.append(pwm_led)
    try:        
        for duty in range(0,65565, 1500):
            for pwm_led in pwm_leds:
                pwm_led.duty_u16(duty)
            sleep_ms(50)
            
        for duty in range(65565,0, -1500):
            for pwm_led in pwm_leds:
                pwm_led.duty_u16(duty)
            sleep_ms(50)   
    finally:
        for pwm_led in pwm_leds:
            pwm_led.deinit()
        for led in leds:
            led.init(Pin.OUT)
            led.off()


#----------------------------main část pro provádění a spouštění-----------------------------------
        
while True:
    try:
        leftRight()   
        hadL() 
        breath()   
        hadR()
        
    except KeyboardInterrupt:
        zhasni()
        print("Exit")
        break