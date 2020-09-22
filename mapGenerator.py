import pygame
from opensimplex import OpenSimplex
import numpy as np
import random
from PIL import Image

from noiseGenerator import *


class Map(OpenSimplexNoise):
    '''Class meant to store a noise array and all the methods related to it'''

    def __init__(self, name, width, height, frequency, seed = None):
        #OpenSimplexNoise.__init__(self, name, width, height, frequency, seed = None)

        self.name = name
        self.width = width
        self.height = height
        self.freq = frequency
        self.seed = seed

        #If it is not given, generates and stores the seed
        #Used to generate the noise array.
        if self.seed == None:
            self.seed = random.randint(1, 500)

        #Initialises the noise object using the opensimplex library using the seed
        self.originalNoiseObject = OpenSimplex(seed)

        #Array to store the values we will be using
        #We chose numpy  to learn how to use it and because it is
        #apparently a better choice
        self.noiseArray = np.empty([width, height])


    def createAndSaveMapAsPNG(self):
        '''This method generates a PNG image using the noiseArray and saves it'''

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

        img1.save('map.png')

#Test
if __name__ == "__main__":
    noiseTest = Map("mapTest", 500, 500, 3, 5)
    noiseTest.generateNoiseArray()
    noiseTest.mapArbValueToColorValue()
    noiseTest.createAndSaveMapAsPNG()
    noiseTest.saveSeedAsTxtFile()

