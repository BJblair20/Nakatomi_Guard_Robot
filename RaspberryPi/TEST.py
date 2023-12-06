import neopixel
import board
import time

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

def killLights():
    pixels = neopixel.NeoPixel(board.D18, 32)
    pixels = (0,0,0)

if __name__ == '__main__':
    killLights()