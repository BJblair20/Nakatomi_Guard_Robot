
import threading
import os
import faceRec
import time
import lights
import distanceReader
import motor



def runMotor():
    global motorControl
    while not motorControl.is_set():
        print("Running Motor")
        motor.runMotor()
        print("Starting reader")
        distanceReader.main()
        print("Got out of reader")
        motor.turn()
        print("Motor Turned")
        time.sleep(3)

def camera():
    print("GOT CAMERA ")
    global motorControl
    time.sleep(0.5)
    faceRec.start()
    motorControl.set()
    print("FFFFFAAAALSSE")
    motor.stopMotor()


#t1 = threading.Thread(target=lights.soundCue, name='t1')
#t2 = threading.Thread(target=lights.lightsCue, name='t2')

motorControl = threading.Event()

#runMotor()

t1 = threading.Thread(target=runMotor, name='t1')
t2 = threading.Thread(target=camera, name='t2')


t2.start()
time.sleep(10)
t1.start()
 
t1.join()
t2.join()


#runMotor()

#print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFf")
#time.sleep(9)

#killme.togglePP()
#killJohnLenon.toggleJL()
