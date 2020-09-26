'''
This program uses the OpenSimplexNoise class to make a Map class that
additionally has a createAndSaveMapAsPNG method
'''

import pygame
from opensimplex import OpenSimplex
import numpy as np
import random
from PIL import Image

from noiseGenerator import *


class Map(OpenSimplexNoise):
    '''Class used for creating a noise list using methods from OpenSimplexNoise
        to create a map and save it as a PNG
    '''

    def __init__(self, name, width, height, frequency, seed = None):
        OpenSimplexNoise.__init__(self, name, width, height, frequency, seed)

    def createAndSaveMapAsPNG(self, path):
        '''This method generates a color PNG image that looks like a map
            using the noiseArray and saves it
        '''

        deep_blue = (0, 0, 77)
        blue = (0, 168, 255)
        sand = (255, 233, 123)
        greeny = (162, 188, 0) 
        dark_green = (0, 67, 0)
        mountain = (90, 90, 90)
        snow = (255, 255, 255)

        img1 = Image.new('RGBA', (self.width, self.height))
        
        for j in range(len(self.noiseArray)):
            for i in range(len(self.noiseArray[j])):
                #print(self.noiseArray[i][j])
                if self.noiseArray[i][j] <= 5:
                    img1.putpixel((i,j), deep_blue)
                elif self.noiseArray[i][j] <= 20:
                    img1.putpixel((i,j), blue)
                elif self.noiseArray[i][j] <= 30:
                    img1.putpixel((i,j), sand)
                elif self.noiseArray[i][j] <= 60:
                    img1.putpixel((i,j), greeny)
                elif self.noiseArray[i][j] <= 120:
                    img1.putpixel((i,j), dark_green)
                elif self.noiseArray[i][j] <= 149:
                    img1.putpixel((i,j), mountain)
                elif self.noiseArray[i][j] >= 150:
                    img1.putpixel((i,j), snow)

        img1.save(path + self.name + '.png')
        
#Test
if __name__ == "__main__":
    mapTest = Map("mapTest", 500, 500, 3, 5)
    mapTest.generateNoiseArray()
    mapTest.mapArbValueToColorValue()
    mapTest.createAndSaveMapAsPNG('gameImages\ ')
    mapTest.saveSeedAsTxtFile()

