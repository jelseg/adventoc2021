def openInput(filename):
    with open(filename,'r') as file:
        input = [line.strip("\n") for line in file]
    return input

closings = {"(":")","<":">","[":"]","{":"}"}
openings = list(closings.keys())
print(openings)
scores = {")":3,">":25137,"]":57,"}":1197}
correct_score = {")":1,">":4,"]":2,"}":3}

def check_line(line):
    openbrackest = []
    correctpart = ""
    for c in line:
        if c in openings:
            openbrackest.append(c)
            correctpart += c
        elif c == closings[openbrackest.pop()]:
            correctpart += c
        else:
            #print(correctpart)
            return scores[c]
    return 0

def check_corrupted(input):
    s = 0
    for line in input:
        s += check_line(line)
    return s

def correct_line(line):
    s=0

    openbrackest = []
    for c in line:
        if c in openings:
            openbrackest.append(c)
        else:
            openbrackest.pop()
    
    to_add_str = ""
    l = len(openbrackest)
    for i in range(l-1,-1,-1):
        brack = openbrackest[i]
        c = closings[brack]
        to_add_str += c
        s*=5
        s += correct_score[c]

    #print(line + " " + to_add_str)
    #print(s)

    return s

def complete_non_corrupted(input):
    #discard corrupted
    to_correct = []
    for line in input:
        if check_line(line) == 0:
            to_correct.append(line)
    
    scores = []
    for line in to_correct:
        scores.append( correct_line(line) )

    scores.sort()

    l = len(scores)
    i = int(l/2)
    return scores[i]

input = openInput("input.txt")
#print(check_corrupted(input))
print(complete_non_corrupted(input))
