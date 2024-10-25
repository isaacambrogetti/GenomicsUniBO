from knapsack_tests import testKnapsackCorrectness
import cProfile

def nextVertex(choice, level):
    if level < len(choice):
        choice[level] = False
        return [choice, level+1]
    else:
        for i in range(level-1, -1, -1):
            if choice[i] == True:
                choice[i] = None
            elif choice[i] == False:
                choice[i] = True
                return [choice, i+1]
        return [choice, 0]

def bypass(choice, level):
    for i in range(level-1, -1, -1):
        if choice[i] == False:
            choice[i] = True
            return [choice, i+1]
        if choice[i] == True:
            choice[i] = None
    return [choice, 0]

def totalSize(sizes, choice, level):
    weight = 0
    for i in range(level):
        if choice[i]:
            weight += sizes[i]
    return weight

def totalUtility(utilities, choice, level):
    utility = 0
    for i in range(level):
        if choice[i]:
            utility += utilities[i]
    return utility


def booleanListToSet(choice):
    result = set()
    for i in range(len(choice)):
        if choice[i]:
            result.add(i)
    return result 

def solveKnapsack(capacity, numberOfItems, sizes, utilities):
    combination, level = nextVertex([None for _ in range(numberOfItems)], 0)
    bestUtility = 0
    while level != 0:
        if totalSize(sizes, combination, level) <= capacity:
            if level == len(sizes):
                if totalUtility(utilities, combination, level) > bestUtility:
                    bestSet = booleanListToSet(combination)
                    bestUtility = totalUtility(utilities, combination, level)
            combination, level = nextVertex(combination, level)
        else:
            combination, level = bypass(combination, level)   
    return bestSet



testKnapsackCorrectness("medium")
#print(nextVertex([True, True, True, True], 4))
'''
a1 = [None, None, None, None]
a2 = 0
for i in range(32):
    a1, a2 = bypass(a1, a2)
    print(a1, a2)'''