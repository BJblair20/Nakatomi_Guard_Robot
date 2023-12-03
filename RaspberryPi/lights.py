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

def soundCue():
    while True:
        audio_file = os.path.dirname(__file__) + '/Sound/alarmSound.wav'
        playsound(audio_file)
    #print(audio_file)
    #my_sound = pygame.mixer.Sound(audio_file)
    #my_sound.play()



if __name__ == '__main__':
    #pygame.init()
    soundCue()