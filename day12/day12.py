
from typing import NoReturn


def openInput(filename):
    with open(filename,'r') as file:
        input = [line.strip("\n").split("-") for line in file]
    return input


'''
class cave:
    def __init__(self,name):
        self.name = name
        self.connections = [] #store cave names to witch it connects

        if self.name != "start" and self.name != "end":
            if self.name.isupper():
                self.small = False
            else:
                self.small = True
        else:
            self.small = True


def get_cave(name, caves):
    for c in caves:
        if name == c.name:
            return c
    return False

def make_connections(input):
    caves = []
    for con in input:
        c = get_cave(con[0],caves)
        if c:
            c.connections.append(con[1])
        else:
            c = cave(con[0])
            c.connections.append(con[1])
            caves.append(c)
        c = get_cave(con[1],caves)
        if c:
            c.connections.append(con[0])
        else:
            c = cave(con[1])
            c.connections.append(con[0])
            caves.append(c)
    return caves
'''

def make_connections(input):
    connections = {}
    for con in input:
        if con[0] in connections:
            connections[con[0]].append(con[1])
        else:
            connections[con[0]] = [con[1]]
        if con[1] in connections:
            connections[con[1]].append(con[0])
        else:
            connections[con[1]] = [con[0]]
    return connections

def N_of_routes(caves,currentcavename,route):
    if currentcavename == "end":
        route += "-" + currentcavename
        print(route)
        return 1
    if not currentcavename in caves:
        print(currentcavename + " does not exist")
        return 0
    if not currentcavename.isupper():
        if currentcavename in route:
            return 0
    if currentcavename == "start":
        route = "start"
    else:
        route += "-" + currentcavename
    s = 0
    for c in caves[currentcavename]:
        s += N_of_routes(caves,c,route)
    return s
    

input = openInput("test_input2.txt")
caves = make_connections(input)
#print(get_cave("A",caves).connections)
print(N_of_routes(caves,"start",""))