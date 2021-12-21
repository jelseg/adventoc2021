
def gameWinner(playerScores):
    for i,score in enumerate(playerScores):
        if score >= 1000:
            return i
    return -1


def part1():
    playerpositions = [3,7] #is input - 1 -> will have positions 0-9, will also call it player 0 and player 1 istead of 1 and 2 for obvious reasons
    playerscores = [0,0]

    dierolls = 0
    diem1 = -1
    l = len(playerpositions)
    turn = 0
    while gameWinner(playerscores) == -1:
        for i in range(3):
            diem1 +=1
            diem1 %= 100
            dierolls += 1
            playerpositions[turn] += diem1 +1
            playerpositions[turn] %= 10
        playerscores[turn] += playerpositions[turn] + 1
        turn += 1
        turn %= l

    winner = gameWinner(playerscores)
    print(playerscores[(winner+1)%l])
    print(dierolls)
    return playerscores[(winner+1)%l]*dierolls


def combos():
    times = {i:0 for i in range(3,10)}
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                times[i+j+k] += 1
    return times

combs = combos()
print(combs)


def wins_all_universes(pos1,pos2,score1,score2,turn=-1):

    if turn == 0:
        score1 += pos1 +1
        w1=0
        w2=0

        if score1 >= 21:
            return 1,0

        for i,times in combs.items():
            w1i,w2i = wins_all_universes(pos1,(pos2+i)%10,score1,score2,(turn+1)%2)
            w1 += times*w1i
            w2 += times*w2i
        return w1,w2
    else:
        if turn > 0:
            score2 += pos2 +1
        w1=0
        w2=0

        if score2 >= 21:
            return 0,1

        for i,times in combs.items():
            w1i,w2i = wins_all_universes((pos1+i)%10,pos2,score1,score2,(turn+1)%2)
            w1 += times*w1i
            w2 += times*w2i
        return w1,w2

print(wins_all_universes(8,2,0,0))