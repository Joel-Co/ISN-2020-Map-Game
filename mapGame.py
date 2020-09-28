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

def createMap():
    '''Function to generate the map we'll be using in the game'''
    gameMap = Map("gameMap", 500, 500, 3)
    gameMap.generateNoiseArray()
    gameMap.mapArbValueToColorValue()
    gameMap.createAndSaveMapAsPNG('gameImages\ ')
    gameMap.saveSeedAsTxtFile('seeds\ ')


#We execute the map-creating function.
createMap()

#Create the folders we will use to store the map(s) and seed(s).
createDirs("gameImages", "seeds")

