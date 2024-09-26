from knapsack_tests import testKnapsackCorrectness
import cProfile

def nextVertex(choice, level, choice_size, sizes, choice_utility, utilities):
    s = choice_size
    u = choice_utility
    if level < len(choice):
        choice[level] = False
        return [choice, level+1, s, u]
    else:
        for i in range(level-1, -1, -1):
            if choice[i] == True:
                choice[i] = None
                s -= sizes[i]
                u -= utilities[i]
            elif choice[i] == False:
                choice[i] = True
                s += sizes[i]
                u += utilities[i]
                return [choice, i+1, s, u]
        return [choice, 0, s, u]

def bypass(choice, level, choice_size, sizes, choice_utility, utilities):
    s = choice_size
    u = choice_utility
    for i in range(level-1, -1, -1):
        if choice[i] == False:
            choice[i] = True
            s += sizes[i]
            u += utilities[i]
            return [choice, i+1, s, u]
        if choice[i] == True:
            choice[i] = None
            s -= sizes[i]
            u -= utilities[i]
    return [choice, 0, s, u]


def booleanListToSet(choice):
    result = set()
    for i in range(len(choice)):
        if choice[i]:
            result.add(i)
    return result 

def remainingUtilities(utilities):
    result = []
    utilitySum = 0
    for i in range(len(utilities)):
        for utility in utilities[i:]:
            utilitySum += utility
        result.append(utilitySum)
        utilitySum = 0
    return result


def solveKnapsack(capacity, numberOfItems, sizes, utilities):
    combination, level, choice_size, choice_utility = nextVertex([None for _ in range(numberOfItems)], 0, 0, sizes, 0, utilities)
    bestUtility = 0
    utilitySum = remainingUtilities(utilities)
    while level != 0:
        bestHopeUtility = choice_utility + utilitySum[level-1]
        if choice_size <= capacity and bestHopeUtility > bestUtility:
            if level == len(sizes):
                if choice_utility > bestUtility:
                    bestSet = booleanListToSet(combination)
                    bestUtility = choice_utility
            combination, level, choice_size, choice_utility = nextVertex(combination, level, choice_size, sizes, choice_utility, utilities)
        else:
            combination, level, choice_size, choice_utility = bypass(combination, level, choice_size, sizes, choice_utility, utilities)   
    return bestSet


testKnapsackCorrectness("large")
#print(bypass([True, False, False, None], 4, 1, [1,2,3,4]))
#print(remainingUtilities([1,2,3,4]))
'''
a1 = [None, None, None, None]
a2 = 0
for i in range(32):
    a1, a2 = bypass(a1, a2)
    print(a1, a2)'''
