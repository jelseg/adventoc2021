import math


class SnailFishgNumber:
    def __init__(self,str_number):
        
        openbrack = 0
        tempnum = ""
        self.numbers = []
        for c in str_number[1:]:
            if c == "[":
                openbrack += 1
            elif c == "]":
                if tempnum != "":
                    self.numbers.append(NumberElement(tempnum,openbrack))
                    tempnum = ""
                openbrack -= 1
            elif c == ",":
                if tempnum != "":
                    self.numbers.append(NumberElement(tempnum,openbrack))
                    tempnum = ""
            else:
                tempnum +=c
    def str2(self) -> str:
        str1 = ""
        str2 = ""
        for el in self.numbers:
            str1 += str(el.numb) + " "
            str2 += str(el.depth) + " "
        return str1 + "\n" + str2

    def explodeFirst(self):
        nnumbers = []
        for i,el in enumerate(self.numbers):
            if el.depth >= 4:
                nnumbers.append(NumberElement(0,el.depth-1))
                if i > 0:
                    nnumbers[i-1].numb += el.numb
                if i < len(self.numbers)-2:
                    self.numbers[i+2].numb += self.numbers[i+1].numb
                    for el2 in self.numbers[i+2:]:
                        nnumbers.append(el2)
                self.numbers = nnumbers
                return True
            else:
                nnumbers.append(el)
        return False
    
    def splitFirst(self):
        nnumbers = []
        for i,el in enumerate(self.numbers):
            if el.numb >= 10:
                n1 = math.floor(el.numb/2)
                n2 = math.ceil(el.numb/2)
                nnumbers.append(NumberElement(n1,el.depth+1))
                nnumbers.append(NumberElement(n2,el.depth+1))
                if i < len(self.numbers)-1:
                    for el2 in self.numbers[i+1:]:
                        nnumbers.append(el2)
                self.numbers = nnumbers
                return True
            else:
                nnumbers.append(el)
        return False
    
    def reduceStep(self):
        if self.explodeFirst():
            return True
        if self.splitFirst():
            return True
        return False
    
    def reduce(self):
        while self.reduceStep():
            pass

    def __add__(self,other):
        result = SnailFishgNumber("")
        result.numbers = [NumberElement(el.numb,el.depth+1) for el in self.numbers]
        for el in other.numbers:
            result.numbers.append(NumberElement(el.numb,el.depth+1))
        
        result.reduce()
        return result
    
    def __str__(self) -> str:
        return str(self.pairUp())

    def pairUp(self):
        pairs = [(el.numb,el.depth) for el in self.numbers]
        for i in range(4,0,-1):
            npairs = []
            pstarted = False
            for j,p in enumerate(pairs):
                if pstarted:
                    pstarted = False
                elif p[1] == i:
                    npairs.append(((p[0],pairs[j+1][0]),p[1]-1))
                    pstarted = True
                else:
                    npairs.append(p)
            pairs = npairs
        return (pairs[0][0],pairs[1][0])

    def pairMagnitude(self,pair):
        mag = 0
        if isinstance(pair[0], int):
            mag += 3* pair[0]
        else:
            mag += 3* self.pairMagnitude(pair[0])
        
        if isinstance(pair[1], int):
            mag += 2* pair[1]
        else:
            mag += 2* self.pairMagnitude(pair[1])
        
        return mag

    def getMagnitude(self):
        return self.pairMagnitude(self.pairUp())
        
    



            

class NumberElement:
    def __init__(self,number_str,depth):
        self.numb = int(number_str)
        self.depth = depth


def openInput(filename):
    with open(filename,'r') as file:
        snNumbers = [SnailFishgNumber(line.strip("\n")) for line in file]
    return snNumbers 

def exc1():
    snNumbers = openInput("input.txt")
    total = snNumbers[0]
    for n in snNumbers[1:]:
        total += n
        #print(total.str2())
    
    print(total)
    print(total.getMagnitude())

def exc2():
    snNumbers = openInput("test_input.txt")
    maxmag = 0
    for i,n1 in enumerate(snNumbers):
        for j,n2 in enumerate(snNumbers):
            if i != j:
                n = n1+n2
                m = n.getMagnitude()
                maxmag = max(maxmag,m)
    print(maxmag)
    return maxmag



'''
test = SnailFishgNumber("[[[[4,3],4],4],[7,[[8,4],9]]]")
test2 = SnailFishgNumber("[1,1]")
test += test2
test.reduce()
print(test)

test3 = SnailFishgNumber("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")
print(test3.getMagnitude())
'''
exc2()

test = SnailFishgNumber("[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]")
test2 = SnailFishgNumber("[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]")
test += test2
print(test.getMagnitude())