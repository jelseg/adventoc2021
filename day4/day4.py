
import numpy as np

def openfile(filename):

    boards = []

    with open(filename,'r') as file:
        line = file.readline()
        line = line.strip("\n")
        drawn_numbers = line.split(',')
        drawn_numbers = np.array(drawn_numbers).astype('int')
        file.readline()

        board = []
        for line in file:
            if line == "\n":
                board = np.array(board)
                board = board.astype('int')
                boards.append(board)
                board = []
            else:
                line = line.strip("\n")
                mylist = line.split(" ")
                mylist = list(filter(('').__ne__, mylist))
                board.append(mylist)
        board = np.array(board)
        board = board.astype('int')
        boards.append(board)
        
    return [drawn_numbers,boards]


def printboards(boards):
    for board in boards:
        print(board)
        print("\n")

def draw_number(boards,number):
    for board in boards:
        board[board==number] = -1

def check_win(board):
    for row in board:
        count = np.count_nonzero(row >= 0)
        if count == 0:
            return True
    for column in board.T:
        count = np.count_nonzero(column >= 0)
        if count == 0:
            return True
    return False

def get_winner(drawn_numbers,boards):
    for num in drawn_numbers:
        draw_number(boards,num)
        for board in boards:
            if check_win(board):
                return [num,board]
    return [False,False]

def get_looser(drawn_numbers,boards):
    i=0
    while len(boards) > 1:
        num = drawn_numbers[i]
        i+=1
        draw_number(boards,num)
        newboards = []
        for board in boards:
            if not check_win(board):
                newboards.append(board)
        boards = newboards
    while not check_win(boards[0]):
        num = drawn_numbers[i]
        i+=1
        draw_number(boards,num)
    return [num,boards[0]]


def getscore(board):
    myarr = board.copy()
    myarr[myarr==-1] = 0
    return np.sum(myarr)

numbers,boards = openfile("input.txt")

#[num,board] = get_winner(numbers,boards)
[num,board] = get_looser(numbers,boards)
printboards([board])
print(getscore(board)*num)