import neopixel
import board
import time

if __name__ == '__main__':

    pixels = neopixel.NeoPixel(board.D18, 32, auto_write=False)
    pixels.brightness = .5
    
    pixels = (255,211,0)
    time.sleep(0.5)
    pixels = (0,0,0)