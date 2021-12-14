import numpy as np
from matplotlib import pyplot as plt

def openInput(filename):
    with open(filename,'r') as file:
        dot_positions = []
        line = file.readline()
        while line != '\n':
            line = line.strip("\n")
            line = line.split(",")
            dot_positions.append([int(line[0]),int(line[1]) ])
            line = file.readline()

        instructions = []
        for line in file.readlines():
            line = line.strip("\n")
            line = line.split("=")
            if line[0][-1] == "x":
                instructions.append((0,int(line[1])))
            else:
                instructions.append((1,int(line[1])))

    return [dot_positions,instructions]

def fold(dots,instruction):
    newdots = []
    for dot in dots:
        ndot = dot
        if dot[instruction[0]] > instruction[1]:
            
            ndot[instruction[0]] = 2*instruction[1]-dot[instruction[0]]
        if not ndot in newdots:
            newdots.append(ndot)

    return newdots

def drawdots(dots):
    #find dimensions:
    lx = 0
    ly = 0
    for dot in dots:
        lx = max(lx,dot[0])
        ly = max(ly,dot[1])
    
    drawing = [[1 for x in range(lx+1)] for y in range(ly+1)]
    drawing = np.array(drawing)
    for dot in dots:
        drawing[dot[1],dot[0]] = 8
    
    plt.imshow(drawing, interpolation='nearest')
    plt.show()





dots,instructions = openInput("input.txt")


#print(dots)

for instruction in instructions:
    dots = fold(dots,instruction)

drawdots(dots)
print(len(dots))