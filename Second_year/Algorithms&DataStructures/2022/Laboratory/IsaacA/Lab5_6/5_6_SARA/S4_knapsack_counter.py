# solveKnapsack(capacity (>0, float), numberOfItems (>0, int), sizes (list, float, pos), utilities (list, >0, float))
# returns a set of indeces of items, set of the items taken, should be type Python set
from knapsack_tests import testKnapsackCorrectness

def nextCombination(choice):
    for i in range(len(choice)-1, -1, -1):
        if choice[i] == False:
            choice[i] = True
            return choice
        else:
            choice[i] = False
    return choice

def totalSize(sizes, choice):
    weight = 0
    for i in range(len(sizes)):
        if choice[i]:
            weight += sizes[i]
    return weight

def totalUtility(utilities, choice):
    utility = 0
    for i in range(len(utilities)):
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
    combination = nextCombination([False for _ in range(numberOfItems)])
    bestUtility = 0
    for _ in range(2**numberOfItems):
        if totalSize(sizes, combination) <= capacity:
            if totalUtility(utilities, combination) > bestUtility:
                bestSet = booleanListToSet(combination)
                bestUtility = totalUtility(utilities, combination)
        combination = nextCombination(combination)
    return bestSet



testKnapsackCorrectness("medium")