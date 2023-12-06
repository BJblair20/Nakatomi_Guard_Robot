import pygame
import os
import subprocess
audio_file = os.path.dirname(__file__) + '/Sound/alarmSound.wav'
#aplay sound.wav

subprocess.run(["su","pi"])
subprocess.run(["whoami"])
subprocess.run(["aplay", audio_file]) 