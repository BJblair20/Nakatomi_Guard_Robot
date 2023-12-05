
import threading
import os

import time
import lights
import distanceReader
import motor



def runMotor():
    global motorControl
    while motorControl == True:
        print("Running Motor")
        motor.runMotor()
        print("Starting reader")
        distanceReader.main()
        print("Got out of reader")
        motor.turn()
        print("Motor Turned")

def camera():
    global motorControl
    i =0
    while i < 10:
        print("I: " + str(i))
        i+=1
    motorControl = False


#t1 = threading.Thread(target=lights.soundCue, name='t1')
#t2 = threading.Thread(target=lights.lightsCue, name='t2')

global motorControl
motorControl = True

t1 = threading.Thread(target=runMotor, name='t1')
t2 = threading.Thread(target=camera, name='t2')

t1.start()
t2.start()
 
t1.join()
t2.join()

#runMotor()

#print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFf")
#time.sleep(9)

#killme.togglePP()
#killJohnLenon.toggleJL()
