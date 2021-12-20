import numpy as np
from matplotlib import pyplot as plt


def openInput(filename):

    with open(filename,'r') as file:
        line = file.readline()
        line = line.strip('\n')
        enhancementArray = ['1' if c == "#" else '0' for c in line]
        file.readline()

        image = [['1' if c=="#" else '0' for c in line.strip("\n")] for line in file]
    image = Image(image)
    return enhancementArray,image

class Image:
    def __init__(self,array):
        self.array = np.array(array)
        self.lx,self.ly = self.array.shape
        self.outside = '0'

    def draw(self):
        narray = self.array.astype('int')
        plt.imshow(narray,interpolation='nearest')
        plt.show()

    def __getitem__(self,indici):
        x = indici[0]
        y = indici[1]
        if x < 0:
            return self.outside
        if y < 0:
            return self.outside
        if x >= self.lx:
            return self.outside
        if y >= self.ly:
            return self.outside
        return self.array[x,y]
    
    def getEnhancedNumber(self,lookup,i,j):
        binnum = ""
        for x in range(-2,1):
            for y in range(-2,1):
                binnum += self[i+x,j+y]
        ind = int(binnum,base=2)
        return lookup[ind]
    
    def enhanceImage(self,lookup):
        arr = [[self.getEnhancedNumber(lookup,j,i) for i in range(self.lx+2)] for j in range(self.ly + 2)]
        self.array = np.array(arr)
        self.lx,self.ly = self.array.shape

        outsidebin = "".join([self.outside for i in range(9)])
        self.outside = lookup[int(outsidebin,base=2)]

    def numberOfLights(self):
        numbarr = self.array.astype('int')
        return np.sum(numbarr)

def part1():

    enhanc,image = openInput("input.txt")
    #image.draw()

    image.enhanceImage(enhanc)
    image.enhanceImage(enhanc)
    image.draw()
    print(image.numberOfLights())

def part2():
    enhanc,image = openInput("input.txt")
    #image.draw()

    for i in range(50):
        image.enhanceImage(enhanc)

    image.draw()
    print(image.numberOfLights())

part2()