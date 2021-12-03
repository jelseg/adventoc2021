def open_input(filename):
    with open(filename,'r') as file:
        result = []
        for line in file:
            line = line.strip("\n")
            result.append(line)
    return result


def gamma_epsilon(binstr_list):
    l = len(binstr_list[0])
    ones=[0 for i in binstr_list[0]]
    zeros = [0 for i in binstr_list[0]]
    for bin in binstr_list:
        for (i,e) in enumerate(bin):
            if e == "1":
                ones[i] += 1
            elif e == "0":
                zeros[i] += 1
    
    print(ones)
    print(zeros)

    gamma = ""
    epsilon = ""

    for (one,zero) in zip(ones,zeros):
        if one > zero:
            gamma+="1"
            epsilon+="0"
        else:
            gamma+="0"
            epsilon+="1"
    
    return [int(gamma,2),int(epsilon,2)]

'''
input = open_input("input.txt")
print(input[1][1])
[gamma,eps] = gamma_epsilon(input)
print(gamma)
print(eps)
print(gamma*eps)
'''


def one_iter(binstr_list,index,want_most_commen = True):
    ones = []
    zeros = []
    for bin in binstr_list:
        if bin[index] == "1":
            ones.append(bin)
        else:
            zeros.append(bin)
    lo = len(ones)
    lz = len(zeros)

    if lz > lo:
        if want_most_commen:
            return zeros
        else:
            return ones
    elif want_most_commen:
        return ones
    else:
        return zeros

def get_oxyrating(binstr_list,want_most_commen = True):
    result = binstr_list
    lb = len(binstr_list[0])
    i = 0
    while len(result) > 1:
        result = one_iter(result,i,want_most_commen)
        i += 1
        i %= lb
    resnum = result[0]
    print(resnum)
    return int(resnum,2)

input = open_input("input.txt")
oxy = get_oxyrating(input)
CO2 = get_oxyrating(input,False)
print(oxy*CO2)