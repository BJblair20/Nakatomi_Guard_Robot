
import threading
import os
import faceRec
import time
import lights
import distanceReader
import motor
import pandas as pd



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
    color = faceRec.start()
    motorControl.set()
    print("FFFFFAAAALSSE")
    motor.stopMotor()
    print("motor stopped")
    actionLists(int(color))

def actionLists(color):
    print("Got to lists!")
    global data
    threads = []
    print(data)
    if data["light"][int(color)]==1:
        threads.append(threading.Thread(target=lights.lightsAlert, name='t1'))
    if data["sound"][int(color)]==1:
        threads.append(threading.Thread(target=lights.soundCue, name='t1'))
    if data["alarm"][int(color)]==1:
        threads.append(threading.Thread(target=lights.lightsAlarm, name='t1'))
        threads.append(threading.Thread(target=lights.alarmCue, name='t1'))
    if data["greeting"][int(color)]==1:
        threads.append(threading.Thread(target=lights.greeting, name='t1'))

    print("Threads made")
    for t in threads:
        t.start()
        t.join()

    print("Threads joined")

    if data["halt"][int(color)]==1:
        print("NAKATOMI BOT:")
        input("CLEAR TO CONTINUE? ")

    lightControl.set()
    lights.setLights(lightControl)
    


#t1 = threading.Thread(target=lights.soundCue, name='t1')
#t2 = threading.Thread(target=lights.lightsCue, name='t2')

curDir = os.path.dirname(os.path.abspath(__file__))
dir=os.path.join(curDir,"../App")
dat1=dir + "/ActionLists.csv"
global data
data = pd.read_csv(dat1)

motorControl = threading.Event()
lightControl = threading.Event()
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
