
import threading
import os
import faceRec
import time
import lights
import distanceReader
import motor
import pandas as pd
#import pygame
import neopixel
import board
import subprocess

#################################################################################################################
#################.......................LIGHTS.....................................##############################
#################################################################################################################

def lightsAlert():
    print("LIGHTS ALERT")
    audio_file = os.path.dirname(__file__) + '/lightsFiles/alertLights.py'
    while not lightControl.is_set():
        subprocess.run(["sudo", "python3", audio_file])
        time.sleep(1)

def killLights(): 
    print("KILL LIGHTS")
    audio_file = os.path.dirname(__file__) + '/lightsFiles/killLights.py'
    while not lightControl.is_set():
        subprocess.run(["sudo", "python3", audio_file], check=True)

def whiteLights(): 
    print("WHITE LIGHTS")
    audio_file = os.path.dirname(__file__) + '/lightsFiles/whiteLights.py'
    subprocess.run(["sudo", "python3", audio_file], check=True)

def lightsAlarm():
    print("LIGHTS ALARM")
    audio_file = os.path.dirname(__file__) + '/lightsFiles/alarmLights.py'
    while not lightControl.is_set():
        subprocess.run(["sudo", "python3", audio_file], check=True)

#################################################################################################################
#################.......................SOUND.....................................##############################
#################################################################################################################

def soundCue():
    print("ALERT SOUND")
    audio_file = os.path.dirname(__file__) + '/Sound/calm.wav'
    while not lightControl.is_set():
        subprocess.run(["aplay", audio_file],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
        #time.sleep(3)
    """
    pygame.mixer.init()
    audio_file = os.path.dirname(__file__) + '/Sound/calm.wav'
    pygame.mixer.music.load(audio_file)
    while not lightControl.is_set():
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    """

def alarmCue():
    #global motorControl
    print("ALARM SOUND")
    audio_file = os.path.dirname(__file__) + '/Sound/alarmSound.wav'
    #aplay sound.wav
    #import subprocess
    
    while not lightControl.is_set():
        subprocess.run(["aplay", audio_file],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
        #time.sleep(1)
    """
    pygame.mixer.init()
    audio_file = os.path.dirname(__file__) + '/Sound/alarmSound.wav'
    pygame.mixer.music.load(audio_file)
    #while motorControl == True:
    while not lightControl.is_set():
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    """
            

def greeting():
    print("GREETING SOUND")
    audio_file = os.path.dirname(__file__) + '/Sound/welcome.wav'
    subprocess.run(["aplay", audio_file],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 

    """
    print("WELCOME")
    pygame.mixer.init()
    audio_file = os.path.dirname(__file__) + '/Sound/welcome.wav'
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    """
#################################################################################################################
#################........................MOTOR..........................#########################################
#################################################################################################################
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

#################################################################################################################
#################.......................CAMERA.....................................##############################
#################################################################################################################
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
        threads.append(threading.Thread(target=lightsAlert, name='light'))
    if data["sound"][int(color)]==1:
        threads.append(threading.Thread(target=soundCue, name='sound'))
    if data["alarm"][int(color)]==1:
        threads.append(threading.Thread(target=lightsAlarm, name='alarm light'))
        threads.append(threading.Thread(target=alarmCue, name='alarm sound'))
    if data["greeting"][int(color)]==1:
        threads.append(threading.Thread(target=greeting, name='greetingSound'))
        threads.append(threading.Thread(target=whiteLights, name='greetingLight'))

    print("Threads made")
    for t in threads:
        print("Starting " + t.getName())
        t.start()
    print("Threads started")
    """
    for t in threads:
        print("Joining " + t.getName())
        t.join()
    """
        

    print("Threads joined")

    if data["halt"][int(color)]==1:
        print("NAKATOMI BOT:")
        userIn = input("CLEAR TO CONTINUE? ")

    print("GOT line 142 ")
    #time.sleep(4)
    lightControl.set()
    time.sleep(3)
    lightControl.clear()
    
    


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

while True:
    t1 = threading.Thread(target=runMotor, name='t1')
    t2 = threading.Thread(target=camera, name='t2')
    #t3 = threading.Thread(target=alarmCue, name='t3')
    #t4 = threading.Thread(target=lightsAlarm, name='t4')

    #global motorControl
    #motorControl = True

    #alarmCue()
    t2.start()
    time.sleep(10)
    t1.start()
    time.sleep(10)
    t1.join()
    t2.join()

    print("ENDED BOTH MAIN THREADS")
    motorControl.clear()
    
    userIn = input("Continue? ")
    if userIn != 'y':
        break
#t3.start()
#t4.start()
 
    
#t3.join()
#t4.join()


#runMotor()

#print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFf")
#time.sleep(9)

#killme.togglePP()
#killJohnLenon.toggleJL()
