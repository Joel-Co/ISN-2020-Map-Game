'''

This program is meant to store the game.

'''
import os
import pygame
from opensimplex import OpenSimplex
import numpy as np
import random
from PIL import Image

from noiseGenerator import *
from mapGenerator import *

def createDirs(*names):
    for name in names:
        try:
            os.mkdir(name)
        except:
            pass

createDirs("gameImages", "seeds")




def createMap():
    gameMap = Map("mapTest", 500, 500, 3)
    gameMap.generateNoiseArray()
    gameMap.mapArbValueToColorValue()
    gameMap.createAndSaveMapAsPNG('gameImages\ ')
    gameMap.saveSeedAsTxtFile('seeds\ ')

createMap()
