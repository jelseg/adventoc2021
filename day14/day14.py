
def openInput(filename):
    with open(filename,'r') as file:
        template = file.readline().strip("\n")
        file.readline()

        pair_insertions = {line.split(" -> ")[0] : line.strip("\n").split(" -> ")[1] for line in file}

    return template, pair_insertions

def oneStep(template,insertions):
    ns = template[0]
    l = len(template)
    for i in range(l-1):
        ns += insertions[template[i]+template[i+1]]
        ns += template[i+1]
    return ns

def most_less_commen(poly):
    alphabet = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN"
    m = ('a',len(poly)+1)
    M = ('a',0)

    for c in alphabet:
        n = poly.count(c)
        if n < m[1] and n != 0:
            m = (c,n)
        if n > M[1]:
            M = (c,n)
    return m,M

def exc1(t,ins):
    for i in range(40):
        t = oneStep(t,ins)
        print(i)
    
    #print(t)
    m,M = most_less_commen(t)
    print(m)
    print(M)
    return M[1]-m[1]



def get_posible_letters(ins):
    letters = []
    for k,v in ins.items():
        if not k[0] in letters:
            letters.append(k[0])
        if not k[1] in letters:
            letters.append(k[1])
        if not v in letters:
            letters.append(v)
    return letters

def all_after_10_steps(ins):
    ins10 = {}
    for k in ins:
        t = k
        for  i in range(10):
            t = oneStep(t,ins)
        ins10[k] = t
    return ins10

def one_after_20_steps(k,ins10):
    t = ins10[k]
    l = len(t)
    res = t[0]
    for i in range(l-1):
        ta = ins10[t[i] + t[i+1]]
        res += ta[1:]
    return res


def all_after_20_steps(ins):
    ins10 = all_after_10_steps(ins)
    ins20 = {}
    for k in ins10:
        ins20[k] = one_after_20_steps(k,ins10)
    
    return ins20

def get_scoreLookup(ins,allletters):
    score_lookup = {}
    for k,v in ins.items():
        score = {}
        for c in allletters:
            score[c] = v[1:].count(c)
        score_lookup[k] = score
    return score_lookup


def result40_1pair(pair,ins20, scores,scorelookup20):
    t = ins20[pair]
    l = len(t)
    for i in range(l-1):
        thisscore = scorelookup20[t[i]+t[i+1]]
        for k in scores:
            scores[k] += thisscore[k]

def initscores(startpoly,ins):
    letters = get_posible_letters(ins)

    scores = {}
    for c in letters:
        scores[c] = 0
    scores[startpoly[0]] = 1
    return scores

def exc2(poly,ins):
    scores = initscores(poly,ins)
    ins20 = all_after_20_steps(ins)
    allletters = get_posible_letters(ins)
    scorelookup20 = get_scoreLookup(ins20,allletters)
    print(scorelookup20)

    l = len(poly)
    for i in range(l-1):
        result40_1pair(poly[i]+poly[i+1],ins20, scores,scorelookup20 )
    
    return scores




t,pi = openInput("input.txt")
#print(pi)
#print(oneStep(t,pi))
#print(exc2(t,pi))
#print(get_posible_letters(pi))
#a10 = all_after_10_steps(pi)
scores = exc2(t,pi)
print(scores)
print(max(scores.values())-min(scores.values()))