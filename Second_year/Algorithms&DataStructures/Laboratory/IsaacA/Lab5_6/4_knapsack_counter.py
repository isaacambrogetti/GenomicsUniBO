from knapsack_tests import testKnapsackCorrectness

def nextCombination(choice):
    for i in range(len(choice)-1, -1, -1):
            if choice[i]:
                choice[i] = False
            else:
                choice[i] = True
                return choice
    return choice

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
    combination = nextCombination(choice)
    for _ in range(2**numberOfItems):
        choice_weight = totalSize(sizes, combination)
        if choice_weight <= capacity:
            choice_value = totalutility(utilities, combination)
            if choice_value > maxValue:
                maxValue = choice_value
                maxCombination = combination.copy()
        combination = nextCombination(choice)
    
    return booleanListToSet(maxCombination)

testKnapsackCorrectness("medium")