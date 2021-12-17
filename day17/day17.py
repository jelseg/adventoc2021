import numpy as np
from matplotlib import pyplot as plt

#target = {'xmin':20, 'xmax':30, 'ymin':-10,'ymax':-5}
target = {'xmin':230, 'xmax':283, 'ymin':-107,'ymax':-57}


def drawTrajectory(positions,target):
    lx = target['xmax']+1
    ly = -target['ymin']+1

    ofset = get_maxy(positions)

    ly += ofset

    drawing = np.zeros((lx,ly))


    for i in range(target["xmin"],target["xmax"]+1):
        for j in range(ofset-target["ymax"],ofset-target["ymin"]+1):
            drawing[i,j] = 0.5

    for pos in positions:
        i = pos[0]
        j = ofset-pos[1]
        drawing[i,j] = 1

    plt.imshow(drawing.T, interpolation='nearest')
    plt.show()


def get_maxy(positions):
    my = 0
    for pos in positions:
        my = max(my,pos[1])
    return my


def get_trajectory(startvel,target):
    pos = (0,0)
    positions = []
    vx = startvel[0]
    vy = startvel[1]
    while pos[0] <= target["xmax"] and pos[1] >= target["ymin"]:
        positions.append(pos)
        pos = (pos[0]+vx,pos[1]+vy)
        if vx > 0:
            vx -= 1
        vy -= 1
        if pos[0] >= target["xmin"] and pos[0] <= target["xmax"] and pos[1] >= target["ymin"] and pos[1] <= target["ymax"]:
            positions.append(pos)
            return positions,'ok'
    if pos[0] > target["xmax"]:
        return positions,'x'
    else:
        return positions,'y'


def getvxformax(target):
    #gets vx so just drops down in the target
    vx = 1
    x = 0
    while x < target["xmin"]:
        x += vx
        vx += 1
    return vx-1

def getvyformax(target):
    #get vy so it doesn't overshoot the target when falling down
    return -target["ymin"]-1

def exc1(target):
    vx = getvxformax(target)
    vy = getvyformax(target)
    print("starting guess: " + str(vx) + "," + str(vy))


    traj,hit = get_trajectory((vx,vy),target)

    while hit != 'ok':
        if hit == 'x':
            vx -= 1
        else:
            vy -= 1
        traj,hit = get_trajectory((vx,vy),target)
    
    print("correct velovity: "+str(vx)+","+str(vy))

    print(get_maxy(traj))
    drawTrajectory(traj,target)


def exc2brute(target):
    count = 0
    vymx = getvyformax(target)+1
    vymin = target["ymin"]
    vxmin = getvxformax(target)
    vxmax = target["xmax"]+1

    for i in range(vxmin,vxmax):
        for j in range(vymin,vymx):
            traj,hit = get_trajectory((i,j),target)
            if hit == 'ok':
                count += 1

    return count

print(exc2brute(target))