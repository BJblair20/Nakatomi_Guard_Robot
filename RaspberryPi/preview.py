import pygame
import os

pygame.mixer.init()
audio_file = os.path.dirname(__file__) + '/Sound/alarmSound.wav'
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue