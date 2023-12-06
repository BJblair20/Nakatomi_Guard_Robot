import pygame
import os
import subprocess
audio_file = os.path.dirname(__file__) + '/Sound/alarmSound.wav'

import subprocess

def get_current_user():
    try:
        result = subprocess.run(['whoami'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f'Error getting current user: {e}')
        return None
    
def change_user(new_user):
    try:
        subprocess.run(['sudo', '-u', new_user, 'ls'])
        print(f'Successfully switched to user: {new_user}')
    except subprocess.CalledProcessError as e:
        print(f'Error switching user: {e}')

if __name__ == "__main__":
    new_user = "pi"
    change_user(new_user)
    print("OUTPUT: " + get_current_user())
    subprocess.run(['whoami'])