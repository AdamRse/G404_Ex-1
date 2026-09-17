import math
import os
import random
import time
import numpy as np


char="//////////////////////////////////////////////////////////////////////////////////////////////"
vitesse=0.01

max_width=math.trunc(os.get_terminal_size().columns)-len(char)
position=max_width//2
turnLimits=[11, 31, 41]
while True:
    turnRate=random.randint(1,50)
    turnRate+=51-random.randint(1,50)
    #turnRate=random.randint(1,100) # Biais de sélection des petits nombres ?

    if turnRate <= turnLimits[2] or turnRate >= 100-turnLimits[2]:
        if turnRate <= turnLimits[0]:
            position-=3
        elif turnRate <= turnLimits[1]:
            position-=2
        elif turnRate <= turnLimits[2]:
            position-=1
        elif turnRate >= 100-turnLimits[2]:
            position+=1
        elif turnRate >= 100-turnLimits[1]:
            position+=2
        else:
            position+=3

    if position < 0:
        position = 1
    elif position > max_width:
        position = max_width-1

    print((" "*(position))+char)

    time.sleep(vitesse)
