'''

This program is meant to store the game.
Currently it creates the folders for images and seeds and
creates the map

'''

#We import the modules we are going to use.
import os
import pygame
from opensimplex import OpenSimplex
import numpy as np
import random
from PIL import Image

#We import the classes from our noiseGenerator and mapGenerator files.
from noiseGenerator import *
from mapGenerator import *


def createDirs(*names):
    '''This function takes an arbitrary number of strings and creates
    directories with those names if they do not exist'''

    for name in names:
        try:
            os.mkdir(name)
        except:
            pass

octaves = {0.5 : 2,
           #1 : 1,
           2 : 0.5,
           4 : 0.25,
           8 : 0.125,
           16 : 0.0625
           }

def createMap(name, width, height, freq, octaves, seed = None):
    '''Function to generate the map we'll be using in the game'''
    gameMap = Map(name, width, height, freq, octaves, seed)
    gameMap.generateNoiseArray()
    gameMap.mapArbValueToColorValue()
    gameMap.saveAsPNG('gameImages\ ')
    gameMap.createAndSaveMapAsPNG('gameImages\ ')
    gameMap.saveSeedAsTxtFile('seeds\ ')
    
#Create the folders we will use to store the map(s) and seed(s).
createDirs("gameImages", "seeds")

#We execute the map-creating function.
createMap("gameMap", 500, 500, 5, octaves)


