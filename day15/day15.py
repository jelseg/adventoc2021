import numpy as np
import time


def openInput(filename):
    with open(filename,'r') as file:
        result = np.array([[c for c in line.strip("\n")] for line in file])
    result = result.astype('int')
    return result

def min_kneighbours(ar,i,j,lx,ly):
    m = 30000
    if i > 0:
        m = min(ar[i-1,j],m)
    if j > 0:
        m = min(ar[i,j-1],m)
    if i < lx-1:
        m = min(ar[i+1,j],m)
    if j < ly-1:
        m = min(ar[i,j+1],m)
    return m

def getTotalRisk(field):
    maxrisk = np.sum(field)
    lx,ly = field.shape
    trisk = np.ones(field.shape)*maxrisk
    trisk[lx-1,ly-1] = field[lx-1,ly-1]
    searching = True

    while searching:
        ntrisk = trisk.copy()

        for i in range(lx-1,-1,-1):
            for j in range(ly-1,-1,-1):
                m = min_kneighbours(ntrisk,i,j,lx,lx)
                ntrisk[i,j] = min(ntrisk[i,j], m+field[i,j])

        if np.all(trisk == ntrisk):
            searching = False
        trisk = ntrisk
    
    return trisk

def exc1(field):
    Trisk = getTotalRisk(field)
    return Trisk[0,0]-field[0,0]

def completefield(incfield):
    row1 = incfield.copy()
    a = field.copy()
    for i in range(4):
        a += 1
        a[a==10] = 1
        row1 = np.append(row1,a,0)
    row1 %= 10
    compfield = row1.copy()
    a = row1.copy()
    for  i in range(4):
        a += 1
        a[a==10] = 1
        compfield = np.append(compfield,a,1)
    
    compfield %= 10
    return compfield

def exc2(field):
    field = completefield(field)
    Trisk = getTotalRisk(field)
    return Trisk[0,0]-field[0,0]

    
tic = time.process_time()
field = openInput("input.txt")
#lx,ly = field.shape
#Trisk = getTotalRisk(field)
#print(exc1(field))
#print(completefield(field).shape)
exc1(field)
toc = time.process_time()
print(toc-tic)
exc2(field)
toc2 = time.process_time()
print(toc2-toc)