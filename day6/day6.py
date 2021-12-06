def open_input(filename):
    with open(filename,'r') as file:
        input = file.readline()
    
    input = input.strip("\n")
    input = input.split(",")
    input = [int(i) for i in input]
    return input

def input_to_fish_per_timer(input):
    fish = [0 for i in range(9)]
    for i in input:
        fish[i] += 1
    return fish

def fish_next_day(fish_today):
    fish = [fish_today[i+1] for i in range(8)]
    fish[6] += fish_today[0]
    fish.append(fish_today[0])
    return fish

def fish_after_N_days(fish_today,N):
    fish = [i for i in fish_today]
    for i in range(N):
        fish = fish_next_day(fish)
    return fish
def count_fishes(fishes):
    s = 0
    for i in fishes:
        s += i
    return s

input = open_input("input.txt")
print(input)
fishes = input_to_fish_per_timer(input)
print(fishes)
fish_end = fish_after_N_days(fishes,256)
print(fish_end)
print(count_fishes(fish_end))
