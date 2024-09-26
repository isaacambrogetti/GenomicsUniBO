from knapsack_tests import testKnapsackCorrectness

def nextVertex(choice, level):
    if level == len(choice)-1:
        if choice[level] == False:
            choice[level] = True
            return (choice, level)
        else:
            while choice[level] != False:       # solves the problem of the skipping already done nodes
                choice[level] = None
                level -= 1
            choice[level] = True
            return (choice, level)
    if choice[level+1] == None:
        level += 1
        choice[level] = False
        return (choice, level)
    if choice[level] == False :
        choice[level] = True
        return (choice, level)

def bypass(choice, level):
    final = [True for _ in range(len(choice))]
    if final == choice:
        return None
    return nextVertex(choice, level)

def totalSize(sizes, choice):
    tot = 0
    for i in range(len(sizes)):
        if choice[i]:
            tot += sizes[i]
    return tot                  #total size of the subset of itmes represented in the list choice

def totalutility(utilities, choice):
    tot = 0
    for i in range(len(utilities)):
        if choice[i]:
            tot += utilities[i]
    return tot

def booleanListToSet(choice):
    setResult = set()
    for i in range(len(choice)):
        if choice[i]:
            setResult.add(i)
    return setResult

def solveKnapsack(capacity, numberOfItems, sizes, utilities):
    maxValue = 0
    allFalse = [False for _ in range(numberOfItems)]
    choice = [False for _ in range(numberOfItems)]
    combination = nextVertex(choice)
    for _ in range(2**numberOfItems):
        choice_weight = totalSize(sizes, combination)
        if choice_weight <= capacity:
            choice_value = totalutility(utilities, combination)
            if choice_value > maxValue:
                maxValue = choice_value
                maxCombination = combination.copy()
        combination = nextVertex(choice)
    
    return booleanListToSet(maxCombination)

#testKnapsackCorrectness("small")       ----- 5.6 -----
#print(bypass([None, True, False], 2))