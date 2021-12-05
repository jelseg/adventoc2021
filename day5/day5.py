import numpy as np

def open_input(filename):
    with open(filename,'r') as file:
        #segments = [line.strip('\n').split(" -> ") for line in file]
        #segments = [[cords[0].split(","),cords[1].split(",")] for cords in [line.strip('\n').split(" -> ") for line in file] ]
        segments = [LineSegment(line.strip("\n")) for line in file]
    return segments

class LineSegment:
    def __init__(self,coords_str):
        coords = coords_str.split(" -> ")
        coords = [coords[0].split(","),coords[1].split(",")]
        self.x0 = int(coords[0][0])
        self.y0 = int(coords[0][1])
        self.x1 = int(coords[1][0])
        self.y1 = int(coords[1][1])
    def __str__(self):
        return f"({self.x0},{self.y0}) -> ({self.x1},{self.y1})"
    def maxX(self):
        return max(self.x0,self.x1)
    def maxY(self):
        return max(self.y0,self.y1) 
        return (self.x0 == self.x1)
    def isVert(self):
        return (self.y0 == self.y1)
    def xRange(self):
        if self.x0 > self.x1:
            return range(self.x0,self.x1-1,-1)
        else:
            return range(self.x0,self.x1 +1 )
    def yRange(self):
        if self.y0 > self.y1:
            return range(self.y0,self.y1-1,-1)
        else:
            return range(self.y0,self.y1+1)
    
    def add_to_field(self,field):
        if self.isVert():
            for i in self.xRange():
                field[i,self.y0] += 1
        elif self.isHor():
            for i in self.yRange():
                field[self.x0,i] += 1
        else:
            for i,j in zip(self.xRange(),self.yRange()):
                field[i,j] += 1

def add_all_lines(segments,field):
    for segment in segments:
        segment.add_to_field(field)
        

def get_field_dimensions(segments):
    mx = 0
    my = 0
    for segment in segments:
        mx = max(mx,segment.maxX())
        my = max(my,segment.maxY())
    return (mx+1,my+1)

def get_empty_field(segments):
    return np.zeros(get_field_dimensions(segments))

def get_score(field):
    return np.count_nonzero(field >= 2)

segments = open_input("input.txt")
#print(segments[2])

field = get_empty_field(segments)
#segments[2].add_to_field(field)
add_all_lines(segments,field)
#print(field.T)

print(get_score(field))
#print(segments[2].isVert())