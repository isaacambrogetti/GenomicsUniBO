from knapsack_tests import testKnapsackCorrectness
import cProfile

def nextVertex(choice, level, choice_size, sizes):
    s = choice_size
    if level < len(choice):
        choice[level] = False
        return [choice, level+1, s]
    else:
        for i in range(level-1, -1, -1):
            if choice[i] == True:
                choice[i] = None
                s -= sizes[i]
            elif choice[i] == False:
                choice[i] = True
                s += sizes[i]
                return [choice, i+1, s]
        return [choice, 0, s]

def bypass(choice, level, choice_size, sizes):
    s = choice_size
    for i in range(level-1, -1, -1):
        if choice[i] == False:
            choice[i] = True
            s += sizes[i]
            return [choice, i+1, s]
        if choice[i] == True:
            choice[i] = None
            s -= sizes[i]
    return [choice, 0, s]


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
    combination, level, choice_size = nextVertex([None for _ in range(numberOfItems)], 0, 0, sizes)
    bestUtility = 0
    while level != 0:
        if choice_size <= capacity:
            if level == len(sizes):
                if totalUtility(utilities, combination, level) > bestUtility:
                    bestSet = booleanListToSet(combination)
                    bestUtility = totalUtility(utilities, combination, level)
            combination, level, choice_size = nextVertex(combination, level, choice_size, sizes)
        else:
            combination, level, choice_size = bypass(combination, level, choice_size, sizes)   
    return bestSet


testKnapsackCorrectness("large")
#print(bypass([True, False, False, None], 4, 1, [1,2,3,4]))
'''
a1 = [None, None, None, None]
a2 = 0
for i in range(32):
    a1, a2 = bypass(a1, a2)
    print(a1, a2)'''