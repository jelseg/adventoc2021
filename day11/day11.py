
import numpy as np

def openInput(filename):
    with open(filename,'r') as file:
        input = [[c for c in line.strip("\n")] for line in file]
    input = np.array(input)
    input = input.astype('int')
    return input


def OneStep(field):
    flashes = np.ones(field.shape)

    field += 1

    temp = field*flashes
    indici = np.where(temp > 9)
    l = len(indici[0])
    indici = zip(indici[0],indici[1])
    while(l > 0):
        for x,y in indici:
            RecordFlash(field,flashes,x,y)
            temp = field*flashes
            indici = np.where(temp > 9)
            l = len(indici[0])
            indici = zip(indici[0],indici[1])

    #put flashed to 0
    field[flashes == -1] = 0
    return np.count_nonzero(flashes == -1)

def RecordFlash(field,flashes,x,y):
    flashes[x,y] = -1
    #field[x,y] = 0
    lx,ly = field.shape

    if x > 0:
        field[x-1,y] += 1
        if y > 0:
            field[x-1,y-1] += 1
        if y < ly-1:
            field[x-1,y+1] += 1
    if y > 0: 
        field[x,y-1] += 1
        if x < lx-1:
            field[x+1,y-1] += 1
    if x < lx-1:
        field[x+1,y] += 1
        if y < ly-1:
            field[x+1,y+1] += 1
    if y < ly-1:
        field[x,y+1] += 1


def Nsteps(field,N):
    f = 0
    for i in range(N):
        f += OneStep(field)
    return f

def step_all_flash(field):
    i = 0
    lx,ly = field.shape
    lAll = lx*ly
    f = 0
    while f < lAll:
        f = OneStep(field)
        i+=1
    return i


input = openInput("input.txt")
#print(Nsteps(input,100))
print(step_all_flash(input))
print(input)