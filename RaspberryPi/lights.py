import time
import board
import neopixel
#import pygame
import os, sys
import pygame
import threading
from playsound import playsound


global lightControl

def setLights(lightControl):
    lightControl.set()


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
    pixels = neopixel.NeoPixel(board.D18, 32, auto_write=False)
    pixels.brightness = .5
    while not lightControl.is_set():
        pixels = (255,211,0)
        time.sleep(0.5)
        pixels = (0,0,0)


def lightsAlarm():
    pixels = neopixel.NeoPixel(board.D18, 32)
    pixels.brightness = .5
    while True:
        for x in range (0, 16):
            pixels[x] = (255,0,0)
        time.sleep(.15)
        for x in range (0,16):
            pixels[x] = (0,0,0)
        time.sleep(.1)
        for x in range (0,16):
            pixels[x] = (0,0,255)
        for x in range (16, 32):
            pixels[x] = (0,0,255)
        time.sleep(.15)
        for x in range (16, 32):
            pixels[x] = (0,0,0)
        time.sleep(.1)
        for x in range(16, 32):
            pixels[x] = (255,0,0)

def soundCue():
    pygame.mixer.init()
    audio_file = os.path.dirname(__file__) + '/Sound/calm.wav'
    pygame.mixer.music.load(audio_file)
    while True:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

def alarmCue():
    pygame.mixer.init()
    audio_file = os.path.dirname(__file__) + '/Sound/alarmSound.wav'
    pygame.mixer.music.load(audio_file)
    while not lightControl.is_set():
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

def greeting():
    audio_file = os.path.dirname(__file__) + '/Sound/welcome.wav'
    print("Got to sound?")
    playsound(audio_file)
    
    """
    pygame.mixer.init()
    audio_file = os.path.dirname(__file__) + '/Sound/welcome.wav'
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
        """



if __name__ == '__main__':
    #pygame.init()
    greeting()