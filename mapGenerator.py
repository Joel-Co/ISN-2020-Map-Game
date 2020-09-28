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

    def __init__(self, name, width, height, frequency, octaves, seed = None):
        OpenSimplexNoise.__init__(self, name, width, height, frequency, octaves, seed)

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
                
        img = Image.new('RGBA', (self.width, self.height))
        for j in range(len(self.noiseArray)):
            for i in range(len(self.noiseArray[j])):

                if self.noiseArray[j][i] <= 45:
                    img.putpixel((i, j), deep_blue)
                elif self.noiseArray[j][i] <= 69:
                    img.putpixel((i, j), blue)
                elif self.noiseArray[j][i] <= 81:
                    img.putpixel((i, j), sand)
                elif self.noiseArray[j][i] <= 120:
                    img.putpixel((i, j), greeny)
                elif self.noiseArray[j][i] <= 170:
                    img.putpixel((i, j), dark_green)
                elif self.noiseArray[j][i] <= 209:
                    img.putpixel((i, j), mountain)
                elif self.noiseArray[j][i] >= 210:
                    img.putpixel((i, j), snow)

        img.save(path + self.name + '_map.png')

octaves = {1 : 1,
    2 : 0.5,
    4 : 0.25,
    8 : 0.125}

#Test only if this file is run and not imported
if __name__ == "__main__":
    mapTest = Map("mapTest", 500, 500, 3, octaves, 0)
    mapTest.generateNoiseArray()
    mapTest.mapArbValueToColorValue()
    mapTest.saveAsPNG('gameImages\ ')
    mapTest.createAndSaveMapAsPNG('gameImages\ ')
    mapTest.saveSeedAsTxtFile()

