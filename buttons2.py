from machine import Pin
from utime import sleep_ms

buttonpins = [0,1,2,3]
buttons = []
lastState = []

for pinNum in buttonpins:
    button = Pin(pinNum, Pin.IN, Pin.PULL_DOWN)
    buttons.append(button)
    lastState.append(0)
    
while True:
    for i in range(len(buttons)):
        currentState = buttons[0].value()
        if currentState != lastState[0]:
            if currentState == 1:
                print(f"Tlačítko {buttonpins[0]} je stisknuto")
            else:
                print(f"Tlačítko {buttonpins[0]} je uvolneno")
            lastState[0] = currentState
        sleep_ms(20)