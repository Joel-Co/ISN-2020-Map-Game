'''This program creates a noise array, changes its format and
can save it's seed, save it as an image, display it in pygame.'''


from noiseGenerator import *

class Camouflage(OpenSimplexNoise):
    '''Class meant to store a noise array and all the methods related to it'''

    def __init__(self, name, width, height, frequency, octaves, seed = None):
        self.name = name
        self.width = width
        self.height = height
        self.freq = frequency
        self.seed = seed
        self.octaves = octaves

        #If it is not given, generates and stores the seed
        #Used to generate the noise array.
        if self.seed == None:
            self.seed = random.randint(1, 500)

        #Initialises the noise object using the opensimplex library using the seed
        self.originalNoiseObject = OpenSimplex(self.seed)

        #Array to store the values we will be using
        #We chose numpy  to learn how to use it and because it is
        #apparently a better choice
        self.noiseArray = np.empty([self.height, self.width])


    def saveAsPNG(self, color, path = ""):
        '''This method generates a PNG image using the noiseArray and saves it'''

        img = Image.new('RGBA', (self.width, self.height))
        
        #dark_brown = (46, 31, 14, 255)
        transparent = (255, 255, 255, 0)

        for j in range(len(self.noiseArray)):
            for i in range(len(self.noiseArray[j])):
                if self.noiseArray[j][i] >= 150:
                    #img.putpixel((i, j), dark_brown)
                    img.putpixel((i, j), color)
                else:
                    img.putpixel((i, j), transparent)
                    
        img.save(path + str(self.name) + '_noise.png')


#The format of this dict is explained in the generateNoiseArray mathod definition.
octaves = {
           1 : 1,
           2 : 0.5,
           #4 : 0.25,
           #8 : 0.125
           }


def camouflageTest():
    import os

    colors = [(196, 196, 137, 255), (46, 31, 14, 255), (33, 54, 8, 255)]
    
    for i, color in enumerate(colors):
        noiseTest = Camouflage("noiseTest", 300, 300, 3, octaves)
        noiseTest.generateNoiseArray()
        noiseTest.mapArbValueToColorValue()
        noiseTest.saveAsPNG(color, 'gameImages\ ' + str(i))
        noiseTest.saveSeedAsTxtFile('seeds\ ')

    background = Image.new('RGBA', (300, 300), (0, 0, 0, 255))

    for i, filename in enumerate(os.listdir("gameImages")):
        if filename.endswith("noiseTest_noise.png"):
            img = Image.open('gameImages/' + filename)
            background.paste(img, (0, 0), img)


    background.save('gameImages\camouflageTest.png', "PNG")


#Test, only if this file is run and not imported
if __name__ == "__main__":
    camouflageTest()
