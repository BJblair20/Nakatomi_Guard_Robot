import time
import board
import neopixel
#import pygame
from playsound import playsound
import os, sys

global audioToggle
global lightToggle
audioToggle = False
lightToggle = False

def lightsCue():
    pixels = neopixel.NeoPixel(board.D12, 32, auto_write=False)
    pixels.brightness = .5
    while audioToggle == True:
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
    pixels = neopixel.NeoPixel(board.D12, 32, auto_write=False)
    pixels.brightness = .5
    while audioToggle == True:
        pixels = (255,211,0)
        time.sleep(0.5)
        pixels = (0,0,0)


def lightsAlarm():
    import time
    import board
    import neopixel


    pixels = neopixel.NeoPixel(board.D12, 32)
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
    while True:
        audio_file = os.path.dirname(__file__) + '/Sound/calm.wav'
        playsound(audio_file)

def alarmCue():
    while True:
        audio_file = os.path.dirname(__file__) + '/Sound/alarmSound.wav'
        playsound(audio_file)

def greeting():
    audio_file = os.path.dirname(__file__) + '/Sound/welcome.wav'
    playsound(audio_file)
    #print(audio_file)
    #my_sound = pygame.mixer.Sound(audio_file)
    #my_sound.play()



if __name__ == '__main__':
    #pygame.init()
    soundCue()