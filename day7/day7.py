def open_input(filename):
    with open(filename,'r') as file:
        input = file.readline()
    
    input = input.strip("\n")
    input = input.split(",")
    #print(input)
    input = [int(i) for i in input]
    return input

def get_fuel(positions,alignpos):
    f = 0
    for i in positions:
        f += abs(i-alignpos)
    return f

def get_best_pos(positions):
    m = max(positions)
    minf = len(positions)*m
    minpos = 0
    for pos in range(m):
        f = get_fuel(positions,pos)
        if f < minf:
            minf = f
            minpos = pos
    return [minpos,minf]

def fibo(N):
    s = 0
    for i in range(1,N+1):
        s += i
    return s

def crabfuel(positions,alignpos):
    f = 0
    for i in positions:
        f += fibo(abs(i-alignpos))
    return f

def get_best_pos2(positions):
    m = max(positions)
    minf = len(positions)*m**2
    minpos = 0
    for pos in range(m):
        f = crabfuel(positions,pos)
        if f < minf:
            minf = f
            minpos = pos
    return [minpos,minf]


input = open_input("input.txt")
[pos,minf] = get_best_pos2(input)
print(pos)
print(minf)