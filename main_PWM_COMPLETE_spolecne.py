from machine import Pin, PWM
from utime import sleep_ms

# --- KONSTANTY A NASTAVENÍ ---
MAX_JAS = 65535  # Maximální hodnota pro PWM (100% svit)
MIN_JAS = 0      # Zhasnuto
FREKVENCE = 1000 # Hz --> kolikrát za vteřinu se stihne rozsvítit a zhasnout

# ---------------------------- Inicializace (Vše je PWM) -----------------------------
leds = []

# Vytvoříme rovnou PWM objekty a uložíme je do seznamu
for i in range(4):
    p = PWM(Pin(i))
    p.freq(FREKVENCE)
    p.duty_u16(MIN_JAS) # Pro jistotu zhasneme
    leds.append(p)

# ---------------------------- Wrappery (Pomocné funkce) -----------------------------
# Tyto funkce nám nahrazují .on() a .off()

def zapni(led_obj):
    """Rozsvítí PWM ledku na maximum"""
    led_obj.duty_u16(MAX_JAS)

def vypni(led_obj):
    """Zhasne PWM ledku"""
    led_obj.duty_u16(MIN_JAS)

def zhasni_vse():
    """Zhasne všechny LED v poli"""
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
    led_obj.duty_u16(0)

# ----------------------------- Animační funkce ----------------------------------
def hadR():
    zhasni_vse()
    for led in leds:
        zapni(led)#led.on()
        sleep_ms(200)
        vypni(led)#led.off()

def hadL():
    zhasni_vse()
    for led in reversed(leds):
        zapni(led)#led.on()
        sleep_ms(200)
        vypni(led)#led.off()
        
def blik():
    zhasni_vse()
    for led in leds:
        zapni(led)#led.on()
    sleep_ms(200)
    zhasni_vse()#led.off()
    sleep_ms(50)
    
def breath():
    for duty in range(MIN_JAS, MAX_JAS, 1500):
        for led in leds:
            led.duty_u16(duty)
        sleep_ms(20)
    for duty in range (MAX_JAS, MIN_JAS, -1500):
        for led in leds:
            led.duty_u16(duty)
        sleep_ms(20)
    zhasni_vse()
    
def blik_ob():
        
    zhasni_vse()
    for i in range(2):    
        for i, led in  enumerate(leds):
            if i % 2 == 0:
                zapni(led)
        sleep_ms(200)
        zhasni_vse()
        sleep_ms(200)
        zhasni_vse()
        
    for i in range(2):    
        for i, led in  enumerate(leds):
            if i % 2 != 0:
                zapni(led)
        sleep_ms(200)
        zhasni_vse()
        sleep_ms(200)
        
# ---------------------------- Main část -----------------------------------
        
while True:
    try:
        blik_ob()


        pass
    except KeyboardInterrupt:
        zhasni_vse()
        # Není potřeba dělat deinit, prostě jen zhasneme a ukončíme
        print("Exit")
        break