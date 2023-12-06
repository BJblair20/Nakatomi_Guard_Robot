import pygame
import os
import subprocess
audio_file = os.path.dirname(__file__) + '/Sound/alarmSound.wav'

import subprocess

def change_user(new_user):
    try:
        subprocess.run(['sudo', '-u', new_user, 'ls'])
        print(f'Successfully switched to user: {new_user}')
    except subprocess.CalledProcessError as e:
        print(f'Error switching user: {e}')

if __name__ == "__main__":
    new_user = "pi"
    change_user(new_user)