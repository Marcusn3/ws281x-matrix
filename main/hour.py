#!/usr/bin/python3
# scrolling rainbows and time. uses scrolldisp.py

from scrolldisp import Display
import sidehat, time

sidehat.brightness(0.5)
Display("~R" + time.strftime("%H:%M") + " ~R")
