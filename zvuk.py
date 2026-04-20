from machine import Pin, ADC
from utime import sleep_ms, ticks_diff, ticks_ms

mic = ADC(26)

leds =[]

for i in range(4):
    leds.append(Pin(i, Pin.OUT))
THRESGOLDS = [400,450,600,800]
avg = []


def soundLED(level):
    for i in range (len(THRESGOLDS)):
        if level > THRESGOLDS[i]:
            leds[i].on()
    #for i, lvl in enumerate(THRESGOLDS):
        else:
            leds[i].off()
    


while True:
    try:
        """val = mic.read_u16()
        print(val)
        sleep_ms(100)"""
        
        maxVal = 0
        minVal = 65536
        
        startTime = ticks_ms()
        while ticks_diff(ticks_ms(), startTime) < 50:
            val = mic.read_u16()
            
            if val < minVal: minVal = val
            if val > maxVal: maxVal = val
            
        peakTopeak = maxVal - minVal
        
        if len(avg) > 10 :
            avg.pop(0)
        avg.append(peakTopeak)
        hodnota = sum(avg)/len(avg)
        
        
        soundLED(hodnota)
        print(f"Min: {minVal} Max:{maxVal} Rozdíl: { peakTopeak}  Prumer:{hodnota}")
        sleep_ms(100)
    
    
        
    except KeyboardInterrupt:
        for led in leds:
            led.off()
        break
