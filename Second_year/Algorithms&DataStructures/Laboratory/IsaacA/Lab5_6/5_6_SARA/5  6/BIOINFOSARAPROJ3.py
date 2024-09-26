import random

def getGenome (length = 15):
    genome = "".join(random.choice("AGCT") for i in range(length))
    offset = random.randint(0, length-4)
    substingLen = random.randint(3, length-offset-1)
    substing = genome[offset:offset + substingLen]
    genome += '$'
    print(genome)
    return [genome, substing]

def BWT (genome):
    M = []
    for _ in range(len(genome)):
        M.append(genome)
        genome = genome[1:] + genome[0]
    M.sort()
    printMatrix(M)
    F = [M[i][0] for i in range(len(M))]
    L = [M[i][-1] for i in range(len(M))]
    return [F, L]


def level(L, pos):
    lvl = L.count(L[pos]) - 1
    for i in range(len(L)):
        if i == pos:
            break
        elif L[i] == L[pos]: 
            lvl -= 1 
    return lvl



def reverseBWT (L):
    finishingPos = {'A': L.count('A'),  # dictionary containig the start position of each character in F
         'C': L.count('A') + L.count('C'), 
         'G': L.count('A') + L.count('C')+ L.count('G'), 
         'T': L.count('A') + L.count('C')+ L.count('G') + L.count('T')} 
    
    T = L[0] # the last character of T is always the first charcater of L (because the $ in the lexicographic order the $ comes before the nucletides)
    pos = finishingPos[L[0]] - level(L, 0)
    for _ in range(len(L)-2):
        T += L[pos]
        pos = finishingPos[L[pos]] - level(L, pos)
    T += L[pos]

    return T

def printMatrix(M):
    for i in range(len(M)):
        for j in M[i]:
            print (j, end=' ')
        print()

def printFL (f, l):
    for i in range(len(l)):
        print(f[i], '\t', l[i])




#g = 'AGAAGA$'
#g = getGenome()[0]
g = 'TAACGTAACTTAGCG$'
M = BWT(g)
print(reverseBWT(M[1]))


#print(BWT(getGenome()[0]))
#print(reverseBWT(getGenome()[0]))