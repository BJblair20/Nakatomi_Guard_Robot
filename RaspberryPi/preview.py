import pygame
import os
import subprocess
audio_file = os.path.dirname(__file__) + '/Sound/alarmSound.wav'
#aplay sound.wav

subprocess.run(["sudo","-u","pi"])
subprocess.run(["whoami"])
print("Here?")
subprocess.run(["aplay", audio_file]) 