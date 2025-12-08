from machine import Pin
from utime import ticks_ms, ticks_diff

pin0= Pin(0,Pin.OUT)
pin1= Pin(1,Pin.OUT)
button1=Pin(2,Pin.IN,Pin.PULL_DOWN)
button2=Pin(3,Pin.IN,Pin.PULL_DOWN)

#----- stavové prom+nné
blik_aktivni = False
cas_posled_blik = 0
min_stav_tlacitka = 0
cas_posled_stisku = 0

def brzda():
    """if button1.value() == 1:
        pin0.on()
    else:
        pin0.off()"""
    pin0.value(button1.value())
    
def blinker(aktualni_cas):
    global blik_aktivni
    global cas_posled_blik, cas_posled_stisku, min_stav_tlacitka
    
    stav_tlacitka = button2.value()
    
    if stav_tlacitka == 1 and min_stav_tlacitka == 0 and ticks_diff(aktualni_cas, cas_posled_stisku) > 200:
        blik_aktivni = not blik_aktivni
        cas_posled_stisku = aktualni_cas
        
        if  not blik_aktivni:
            pin1.off
            print("blinker vypnuty")
            
    min_stav_tlacitka = stav_tlacitka
    
    if blik_aktivni and ticks_diff(aktualni_cas, cas_posled_blik) >= 500:
        pin1.toggle()
        cas_posled_blik = aktualni_cas
        print("blik")               
try:
    while True:
        brzda()
        now = ticks_ms
        blinker(now)
                
except KeyboardInterrupt:
        pin0.off()
        pin1.off()