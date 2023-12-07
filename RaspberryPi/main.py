
import threading
import os
import faceRec
import time
import lights
import distanceReader
import motor
import pandas as pd
import pygame
import neopixel
import board
import subprocess

#################################################################################################################
#################.......................LIGHTS.....................................##############################
#################################################################################################################
def lightsCue():
    pixels = neopixel.NeoPixel(board.D18, 32, auto_write=False)
    pixels.brightness = .5
    while not lightControl.is_set():
        for i in range(16):
            pixels[i] = (255,0,0)
            pixels.show()
        for i in range(16,32):
            pixels[i] = (0,0,255)
            pixels.show()
        for i in range(31,0,-1):
            pixels[i]=(0,0,0)
            pixels.show()
        time.sleep(.01)

def lightsAlert():
    print("LIGHTS ALERT")
    pixels = neopixel.NeoPixel(board.D18, 32, auto_write=False)
    pixels.brightness = .5
    while not lightControl.is_set():
        pixels = (255,211,0)
        time.sleep(0.5)
        pixels = (0,0,0)

def killLights():
    pixels = neopixel.NeoPixel(board.D18, 32)
    pixels = (0,0,0)

def lightsAlarm():
    command = "sudo python3 alarmLights.py"
    print(command)
    subprocess.run([command], check=True)

#################################################################################################################
#################.......................SOUND.....................................##############################
#################################################################################################################

def soundCue():
    pygame.mixer.init()
    audio_file = os.path.dirname(__file__) + '/Sound/calm.wav'
    pygame.mixer.music.load(audio_file)
    while not lightControl.is_set():
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

def alarmCue():
    global motorControl
    print("ALARM SOUND")
    audio_file = os.path.dirname(__file__) + '/Sound/alarmSound.wav'
    #aplay sound.wav
    import subprocess

    subprocess.run(["aplay", audio_file]) 
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
    print("WELCOME")
    pygame.mixer.init()
    audio_file = os.path.dirname(__file__) + '/Sound/welcome.wav'
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

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
        threads.append(threading.Thread(target=lightsAlert, name='t1'))
    if data["sound"][int(color)]==1:
        threads.append(threading.Thread(target=soundCue, name='t1'))
    if data["alarm"][int(color)]==1:
        threads.append(threading.Thread(target=lightsAlarm, name='t1'))
        threads.append(threading.Thread(target=alarmCue, name='t1'))
    if data["greeting"][int(color)]==1:
        threads.append(threading.Thread(target=greeting, name='t1'))

    print("Threads made")
    for t in threads:
        t.start()
        t.join()

    print("Threads joined")

    if data["halt"][int(color)]==1:
        print("NAKATOMI BOT:")
        input("CLEAR TO CONTINUE? ")

    print("GOT line 142 ")
    time.sleep(8)
    lightControl.set()
    
    


#t1 = threading.Thread(target=lights.soundCue, name='t1')
#t2 = threading.Thread(target=lights.lightsCue, name='t2')

curDir = os.path.dirname(os.path.abspath(__file__))
dir=os.path.join(curDir,"../App")
dat1=dir + "/ActionLists.csv"
global data
data = pd.read_csv(dat1)

#motorControl = threading.Event()
lightControl = threading.Event()
#runMotor()

#t1 = threading.Thread(target=runMotor, name='t1')
#t2 = threading.Thread(target=camera, name='t2')
t3 = threading.Thread(target=alarmCue, name='t3')
t4 = threading.Thread(target=lightsAlarm, name='t4')

global motorControl
motorControl = True

#alarmCue()
#t2.start()
time.sleep(5)
motorControl = False
#t1.start()
#time.sleep(10)
t3.start()
t4.start()
 
#t1.join()
#t2.join()
t3.join()
t4.join()


#runMotor()

#print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFf")
#time.sleep(9)

#killme.togglePP()
#killJohnLenon.toggleJL()
