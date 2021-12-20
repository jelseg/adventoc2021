import numpy as np

def openInput(filename):
    with open(filename,'r') as file:
        beacons = []
        i = 0
        scanners = []
        for line in file:
            if line == "\n":
                scanners.append(Scanner(beacons))
                beacons = []
            elif line[0:2] == "--":
                pass
            else:
                line = line.strip("\n")
                C = line.split(',')
                beacons.append( [int(c) for c in C ])
        scanners.append(Scanner(beacons))
        return scanners


def getRotationMatrices():
    Rx = np.array([[1,0,0],[0,0,1],[0,-1,0]])
    Ry = np.array([[0,0,-1],[0,1,0],[1,0,0]])
    Rz = np.array([[0,1,0],[-1,0,0],[0,0,1]])

    I = np.array([[1,0,0],[0,1,0],[0,0,1]])

    dirs = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                dirs.append((i,j,k))
    
    Rots = {}
    for dir in dirs:
        rot = I
        for i in range(dir[0]):
            rot = np.dot(Rx,rot)
        for j in range(dir[1]):
            rot = np.dot(Ry,rot)
        for k in range(dir[2]):
            rot = np.dot(Rz,rot)
        Rots[dir] = rot
    
    #REMOVE DOUBLES
    nRots = {}
    for k,v in Rots.items():
        ok = True
        for v2 in nRots.values():
            if np.all(v==v2):
                ok = False
                break
        if ok:
            nRots[k] = v

    return nRots

def checkRotMatrices(matrices):
    doubles = {}
    for k,v in matrices.items():
        c = 0
        nk = []
        for k2,v2 in matrices.items():
            if np.all(v == v2):
                c+= 1
                nk.append(k2)
        if c > 1:
            ks = ""
            for k3 in nk:
                for i in k3:
                    ks+=str(i)
            doubles[ks] = v

    for k,v in doubles.items():
        print(k)
        print(v)
    print(len(matrices))


rotmatrices = getRotationMatrices()

def Rotate(positions,rotation):
    return (np.dot(rotation,positions.T)).T

class Scanner:
    def __init__(self,beacons):
        self.beacons = np.array(beacons)
        self.posKnown = False

        self.possibleOr = {}
        for k,rot in rotmatrices.items():
            self.possibleOr[k] = Rotate(self.beacons,rot)

    def setPosition(self,pos,rot):
        self.pos = pos
        self.posKnown = True
        self.beacons = Rotate(self.beacons,rot) + self.pos

    def checkPosibleOverlap(self,other): #assumes position of other is known
        for k,beaconsRotated in self.possibleOr.items():
            translations = {}
            for beacon in beaconsRotated:
                for otherbeac in other.beacons:
                    trans = otherbeac-beacon

                    tt = ",".join([str(i) for i in trans])

                    if tt in translations:
                        translations[tt] += 1
                    else:
                        translations[tt] = 1

            for tt,v in translations.items():
                if v >= 12:
                    if self.checkOverlap(other,[int(i) for i in tt.split(',')],beaconsRotated):
                        self.pos = [int(i) for i in tt.split(',')]
                        self.beacons = beaconsRotated + self.pos
                        self.posKnown = True
                        return True
            #print(max(translations.values()))

        return False
    
    def checkOverlap(self,other,transpose,rotatedbeacons):
        transBeacons = rotatedbeacons + transpose
        same = 0
        for b in transBeacons:
            for b2 in other.beacons:
                #print(b==b2)
                if np.all( b == b2 ):
                    same+= 1
        #print(same)
        if same >= 12 :
            return True
        
        return False
    
def Part1():
    scanners = openInput("input.txt")
    scanners[0].setPosition([0,0,0],rotmatrices[(0,0,0)])
    foundscanners = [scanners[0]]
    notfound = scanners[1:]
    totfound = 1
    while len(notfound) > 0:
        for i,nfScanner in enumerate(notfound):
            for fScanner in foundscanners:
                if nfScanner.checkPosibleOverlap(fScanner):
                    foundscanners.append(nfScanner)
                    notfound.pop(i)
                    totfound += 1
                    print(totfound)
                    break
    
    allBeacons = []
    for scanner in foundscanners:
        for beacon in scanner.beacons:
            isIn = False
            for compBeacon in allBeacons:
                if np.all(compBeacon == beacon):
                    isIn = True
                    break
            if not isIn:
                allBeacons.append(beacon)

    print(len(allBeacons))

def Part2():
    scanners = openInput("input.txt")
    scanners[0].setPosition([0,0,0],rotmatrices[(0,0,0)])
    foundscanners = [scanners[0]]
    notfound = scanners[1:]
    totfound = 1
    while len(notfound) > 0:
        for i,nfScanner in enumerate(notfound):
            for fScanner in foundscanners:
                if nfScanner.checkPosibleOverlap(fScanner):
                    foundscanners.append(nfScanner)
                    notfound.pop(i)
                    totfound += 1
                    print(totfound)
                    break
    
    scannerpos = [i.pos for i in foundscanners]
    m = 0
    for pos1 in scannerpos:
        for pos2 in scannerpos:
            md = abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1]) + abs(pos1[2]-pos2[2])
            m = max(m,md)
    print(m)
    

Part2()