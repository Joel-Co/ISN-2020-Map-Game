'''

This program is meant to store the game.
Currently it creates the folders for images and seeds and
creates the map

'''

#We import the modules we are going to use.
import os
import sys
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

def rightGo():
    global Xvis
    Xvis = Xvis -1
    screen.blit(MUNDI, [Xvis, Yvis])
    #print ("funciona1")

def leftGo():
    global Xvis
    Xvis = Xvis +1
    screen.blit(MUNDI, [Xvis, Yvis])
    #print ("funciona2")

def downGo():
    global Yvis
    Yvis = Yvis -1
    screen.blit(MUNDI, [Xvis, Yvis])
    #print ("funciona3")

def upGo():
    global Yvis
    Yvis = Yvis +1
    screen.blit(MUNDI, [Xvis, Yvis])
    #print ("funciona4")


def downLimit():
    global Yvis
    global Ysize
    Yvis = Ysize
    screen.blit(MUNDI, [Xvis, Yvis])

def upLimit():
    global Yvis
    Yvis = 0
    screen.blit(MUNDI, [Xvis, Yvis])

def leftLimit():
    global Xvis
    Xvis = 0
    screen.blit(MUNDI, [Xvis, Yvis])

def rightLimit():
    global Xvis
    global Xsize
    Xvis = Xsize
    screen.blit(MUNDI, [Xvis, Yvis])
    
pygame.init()   

Xvis = 0 
Yvis = 0 
Xsize = 500
Ysize = 500
Xmundi = 1000
Ymundi = 1000
size = Xsize, Ysize 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("EXPLORER")

MUNDI0 = pygame.image.load("gameMap_map.png").convert()       
MUNDI = pygame.transform.scale(MUNDI0,(Xmundi,Ymundi))

run=True

while run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: run = False
        
    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    print (str(Mouse_x), str(Mouse_y))
    if Mouse_x >= (Xsize) -100:
        rightGo()
    if Mouse_x <= 100:
        leftGo()
    if Mouse_y >= (Xsize) -100:
        downGo()
    if Mouse_y <= 100:
        upGo()
    if Yvis >= 0:
        upLimit()
    if (Yvis) + (Xmundi) <= Ysize:
        downLimit()
    if Xvis >= 0:
        leftLimit()
    if (Xvis) + (Xmundi) <= Xsize:
        rightLimit()

    screen.blit(MUNDI, [Xvis, Yvis])
    pygame.display.flip()                                  


pygame.quit()


    
#Create the folders we will use to store the map(s) and seed(s).
createDirs("gameImages", "seeds")

#We execute the map-creating function.
createMap("gameMap", 500, 500, 5, octaves)



