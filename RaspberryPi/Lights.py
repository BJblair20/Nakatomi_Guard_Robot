from gpiozero import LED
from time import sleep

#blinking lights code, should work if
#pin is correct

led = LED(18)
bool = True

#purpose is for breaking the alarm loop
def changebool(bool):
    if(bool == True):
        bool = False
    else:
        bool = True

while bool == True:
    led.on()
    sleep(10)
    led.off()
    sleep(10)

