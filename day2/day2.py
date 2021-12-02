def open_input(filename):
    with open(filename,'r') as file:
        directions = []
        for line in file:
            l = line.strip("\n")
            d = l.split(" ")
            #directions.append(d)
            amount = int(d[1])
            dir = [0,0]
            if d[0] == "forward":
                dir=[amount,0]
            elif d[0] == "down":
                dir = [0,amount]
            elif d[0]== "up":
                dir = [0,-amount]
            directions.append(dir)
    return directions

def open_input2(filename):
    with open(filename,'r') as file:
        commands = []
        for line in file:
            l = line.strip("\n")
            d = l.split(" ")
            d[1] = int(d[1])
            commands.append(d)
    return commands



def get_end_pos(directions):
    pos = [0,0]
    for direction in directions:
        pos[0] += direction[0]
        pos[1] += direction[1]
    return pos

def get_end_pos2(commands):
    pos = [0,0]
    aim = 0

    for command in commands:
        if command[0] == "down":
            aim += command[1]
        elif command[0] == "up":
            aim -= command[1]
        elif command[0] == "forward":
            pos[0] += command[1]
            pos[1] += aim*command[1]
    return pos

'''
input = open_input("input1.txt")
endpos = get_end_pos(input)
print(endpos)
print(endpos[0]*endpos[1])
'''

input = open_input2("input1.txt")
endpos = get_end_pos2(input)
print(endpos)
print(endpos[0]*endpos[1])