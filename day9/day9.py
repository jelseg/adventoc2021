import numpy as np

def openInput(filename):
    with open(filename,'r') as file:
        input = [[c for c in line.strip("\n")] for line in file]
    
    input = np.array(input)
    input = input.astype('int')
    return input

def get_lows(heights):
    lx,ly = heights.shape
    lows = []

    for i in range(lx):
        for j in range(ly):
            if is_low(i,j,heights,lx,ly):
                lows.append((i,j))
    return lows

def total_risk_level(positions,heights):
    risk = 0
    for pos in positions:
        risk+=1+heights[pos[0],pos[1]]
    return risk
    
def is_low(x,y,heights,lx,ly):
    h = heights[x,y]
    if x>0:
        if heights[x-1,y] <= h:
            return False
    if x < lx-1:
        if heights[x+1,y] <= h:
            return False
    if y > 0:
        if heights[x,y-1] <= h:
            return False
    if y < ly-1:
        if heights[x,y+1] <= h:
            return False
    return True

def get_basins(heights,lowpoints):
    basinmap = -np.ones(heights.shape)

    lx,ly = heights.shape
    #assign lowpoints to basins:
    for i,point in enumerate(lowpoints):
        basinmap[point[0],point[1]] = i+1
    
    #put heights 9 to no basin (=0)
    for i in range(lx):
        for j in range(ly):
            if heights[i,j] == 9:
                basinmap[i,j] = 0

    while not all_assigned(basinmap):
        for i in range(lx):
            for j in range(ly):
                basinmap[i,j] = check_neighboring_basin(i,j,basinmap,lx,ly)

    return basinmap

def check_neighboring_basin(x,y,basinmap,lx,ly):
    if basinmap[x,y] >=0:
        return basinmap[x,y]
    
    if x > 0:
        if basinmap[x-1,y] > 0:
            return basinmap[x-1,y]
    if x < lx-1:
        if basinmap[x+1,y] > 0:
            return basinmap[x+1,y]
    if y>0:
        if basinmap[x,y-1] > 0:
            return basinmap[x,y-1]
    if y < ly-1:
        if basinmap[x,y+1] > 0:
            return basinmap[x,y+1]
    return -1

def all_assigned(basinmap):
    return np.count_nonzero(basinmap < 0) == 0

def largestbasinsizes(basinmap):
    i = 1
    basinsize = 1
    basinsizes = []
    while basinsize:
        basinsize = np.count_nonzero(basinmap == i)
        print(basinsize)
        basinsizes.append(basinsize)
        i += 1
    basinsizes.sort(reverse = True)
    return basinsizes


input = openInput("input.txt")
lowpoints = get_lows(input)
#print(total_risk_level(lowpoints,input))

basins = get_basins(input,lowpoints)
sizes = largestbasinsizes(basins)
#print(basins)
print(sizes[0]*sizes[1]*sizes[2])
