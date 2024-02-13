import time
import random
import neopixel
import board
import touchio
from prt import *
from morse import *
REPL = True
lnum = 2
langs = ["klingon","vulcan","mandoa"]
lang = langs[lnum]

prt("current: "+lang)

while True:
    val = 0
    if touch1.value:
        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()

    if Val == 1: #advance language
        lnum = lnum + 1
        if lnum >2:
            lnum = 0
        compthink()
        prt("Current lang: "+langs[lnum])

    if Val == 2 : #display words
        for i in range(5):
            prt(wisdom(random.randrange(file_len(langs[lnum])),langs[lnum]))
    time.sleep(.25)

