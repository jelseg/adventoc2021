
def openInput(filename):
    with open(filename,'r') as file:
        input = [line.strip("\n").split("-") for line in file]
    return input


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
        if currentcavename in route.split("-"):
            return 0
    if currentcavename == "start":
        route = "start"
    else:
        route += "-" + currentcavename
    s = 0
    for c in caves[currentcavename]:
        s += N_of_routes(caves,c,route)
    return s

def N_of_routes2(caves,currentcavename,route=[],twice=True):
    route = [r for r in route]
    if currentcavename == "end":
        route.append(currentcavename)
        #print('-'.join(route))
        return 1
    if not currentcavename in caves:
        print(currentcavename + " does not exist")
        return 0
    if not currentcavename.isupper():
        if currentcavename in route:
            if currentcavename == "start":
                return 0
            elif twice:
                twice = False
            else:
                return 0
    
    route.append(currentcavename)
    s = 0
    for c in caves[currentcavename]:
        s += N_of_routes2(caves,c,route,twice)
    return s
    

input = openInput("input.txt")
caves = make_connections(input)
#print(get_cave("A",caves).connections)
print(N_of_routes2(caves,"start"))