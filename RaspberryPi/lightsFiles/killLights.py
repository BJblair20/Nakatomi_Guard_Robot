import neopixel
import board
import time

if __name__ == '__main__':    
    pixels = neopixel.NeoPixel(board.D18, 32)
    for x in range (0,32):
        pixels[x] = (0,0,0)