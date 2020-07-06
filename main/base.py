from rpi_ws281x import *
from time import sleep
from random import randint
import traceback
import argparse
import math
import time

####################################################################

# LED strip configuration:
LED_COUNT = 128        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 10  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

####################################################################

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

####################################################################

wrd_rgb = [[154, 173, 154], [0, 255, 0], [0, 200, 0], [0, 162, 0], [0, 145, 0], [0, 96, 0], [0, 74, 0], [0, 0, 0,]]
clock = 0
blue_pilled_population = [[randint(0,128), 7]]

####################################################################

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i + q, color)
			strip.show()
			time.sleep(wait_ms / 1000.0)
			for i in range(0, strip.numPixels(), 3):
				trip.setPixelColor(i + q, 0)


def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256 * iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i + j) & 255))
		strip.show()
		time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256 * iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(
				(int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i + q, wheel((i + j) % 255))
			strip.show()
			time.sleep(wait_ms / 1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i + q, 0)

#######################################################################

try:
	parser = argparse.ArgumentParser()
	parser.add_argument('-r', '--rainbow', action='store_true', help='make a rainbow')
	parser.add_argument('-d', '--drop', action='store_true', help='rainbow drops')
	parser.add_argument('-u', '--up', action='store_true', help='upsidedown rainbow')
	parser.add_argument('-m', '--matrix', action='store_true', help='matrix')
	parser.add_argument('-s', '--strand', action='store_true', help='strandtest')
	args = parser.parse_args()

#######################################################################

	while True:
		if args.drop:
			for x in range(LED_COUNT):
				r = int((math.cos(x * math.pi / 4) + 1) * 127)
				g = int((math.cos((x - 8.0 / 3.0) * math.pi / 4) + 1) * 127)
				b = int((math.cos((x + 8.0 / 3.0) * math.pi / 4) + 1) * 127)
				for m in range(8):
					strip.setPixelColor(m+x, Color(r, g, b))
					strip.show()
			for l in range(LED_COUNT):
				strip.setPixelColor(l, Color(0, 0, 0))
				strip.show()

####################################################################				

		elif args.matrix:

			for person in blue_pilled_population:
					y = person[1]
					for rgb in wrd_rgb:
							if (y <= 7) and (y >= 0):
									strip.setPixelColor(person[0] - y, Color(rgb[0], rgb[1], rgb[2]))
							y += 1
					person[1] -= 1
			strip.show()
			time.sleep(0.1)
			clock += 1
			if clock % 5 == 0:
					blue_pilled_population.append([randint(0,128), 7])
			if clock % 7 == 0:
					blue_pilled_population.append([randint(0,128), 7])
			while len(blue_pilled_population) > 100:
					blue_pilled_population.pop(0)

#######################################################################

		elif args.up:
			c = 0
			for x in range(16):
				r = int((math.cos(x * math.pi / 4) + 1) * 127)
				g = int((math.cos((x - 8.0 / 3.0) * math.pi / 4) + 1) * 127)
				b = int((math.cos((x + 8.0 / 3.0) * math.pi / 4) + 1) * 127)
				for m in range(8):
					strip.setPixelColor(c + m, Color(r, g, b))
					strip.show()
				c += 8
			for l in range(LED_COUNT):
				strip.setPixelColor(l, Color(0, 0, 0))
				strip.show()

######################################################################

		elif args.rainbow:
			for x in range(LED_COUNT):
				print(x)
				r = int((math.cos(x * math.pi / 4) + 1) * 127)
				g = int((math.cos((x - 8.0 / 3.0) * math.pi / 4) + 1) * 127)
				b = int((math.cos((x + 8.0 / 3.0) * math.pi / 4) + 1) * 127)
				strip.setPixelColor(x, Color(r, g, b))
				strip.show()
			for l in range(LED_COUNT):
				strip.setPixelColor(l, Color(0, 0, 0))
				strip.show()

#######################################################################

		elif args.strand:
			colorWipe(strip, Color(255, 0, 0))  # Red wipe
			colorWipe(strip, Color(0, 255, 0))  # Blue wipe
			colorWipe(strip, Color(0, 0, 255))  # Green wipe
			theaterChase(strip, Color(127, 127, 127))  # White theater chase
			theaterChase(strip, Color(127, 0, 0))  # Red theater chase
			theaterChase(strip, Color(0, 0, 127))  # Blue theater chase
			rainbow(strip)
			rainbowCycle(strip)
			theaterChaseRainbow(strip)

#######################################################################
		else:
			for i in range(LED_COUNT):
				r = randint(1, 255)
				g = randint(1, 255)
				b = randint(1, 255)
				strip.setPixelColor(i, Color(r, g, b))
				strip.show()
			for j in range(LED_COUNT):
				strip.setPixelColor(j, Color(0, 0, 0))
				strip.show()

##############################################################

except:
	print("\nExiting...")
	for k in range(LED_COUNT):
		strip.setPixelColor(k, Color(0, 0, 0))
		strip.show()
