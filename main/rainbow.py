#!/usr/bin/python3
# displays a continuous scrolling rainbow using HSV

#import unicornhat as u
from rpi_ws281x import *
import colorsys, time
# LED strip configuration:
LED_COUNT = 128        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 10  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

i = 0.0
while True:
    i -= 0.002
    for x in range(128):
        r,g,b = colorsys.hsv_to_rgb((i + x / 8.0) % 1,1,1)
        strip.setPixelColor(x,Color(int(r*255),int(g*255),int(b*255)))
    strip.show()
