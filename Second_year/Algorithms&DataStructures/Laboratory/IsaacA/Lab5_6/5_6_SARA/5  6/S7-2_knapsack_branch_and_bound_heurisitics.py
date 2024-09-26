from knapsack_tests import testKnapsackCorrectness
import cProfile

def nextVertex(choice, level, choice_size, sizes, choice_utility, utilities, indeces):
    s = choice_size
    u = choice_utility
    if level < len(choice):
        choice[indeces[level]] = False
        return [choice, level+1, s, u]
    else:
        for i in range(level-1, -1, -1):
            if choice[indeces[i]] == True:
                choice[indeces[i]] = None
                s -= sizes[indeces[i]]
                u -= utilities[indeces[i]]
            elif choice[indeces[i]] == False:
                choice[indeces[i]] = True
                s += sizes[indeces[i]]
                u += utilities[indeces[i]]
                return [choice, i+1, s, u]
        return [choice, 0, s, u]

def bypass(choice, level, choice_size, sizes, choice_utility, utilities, indeces):
    s = choice_size
    u = choice_utility
    for i in range(level-1, -1, -1):
        if choice[indeces[i]] == False:
            choice[indeces[i]] = True
            s += sizes[indeces[i]]
            u += utilities[indeces[i]]
            return [choice, i+1, s, u]
        if choice[indeces[i]] == True:
            choice[indeces[i]] = None
            s -= sizes[indeces[i]]
            u -= utilities[indeces[i]]
    return [choice, 0, s, u]


def booleanListToSet(choice):
    result = set()
    for i in range(len(choice)):
        if choice[i]:
            result.add(i)
    return result 


def densityOrder(numberOfItems, sizes, utilities):
    density = []
    for i in range(numberOfItems):
        density.append((utilities[i]/sizes[i], i))
    density.sort(reverse=True)
    indeces = [i[1] for i in density]
    densities = [i[0] for i in density]
    return [indeces, densities]

def solveKnapsack(capacity, numberOfItems, sizes, utilities):
    indeces, densities = densityOrder(numberOfItems, sizes, utilities)
    combination, level, choice_size, choice_utility = nextVertex([None for _ in range(numberOfItems)], 0, 0, sizes, 0, utilities, indeces)
    bestUtility = 0
    while level != 0:
        if choice_size <= capacity:
            if level == len(sizes):
                if choice_utility > bestUtility:
                    bestSet = booleanListToSet(combination)
                    bestUtility = choice_utility
                combination, level, choice_size, choice_utility = nextVertex(combination, level, choice_size, sizes, choice_utility, utilities, indeces)
            else:
                bestHopeUtility = choice_utility + (capacity-choice_size)*densities[level] # forse va dopo l'if che controlla il livello
                if bestHopeUtility < bestUtility:
                    combination, level, choice_size, choice_utility = bypass(combination, level, choice_size, sizes, choice_utility, utilities, indeces)
                else:
                    combination, level, choice_size, choice_utility = nextVertex(combination, level, choice_size, sizes, choice_utility, utilities, indeces)
        else:
            combination, level, choice_size, choice_utility = bypass(combination, level, choice_size, sizes, choice_utility, utilities, indeces)   
    return bestSet


testKnapsackCorrectness("large")
#print(bypass([True, False, False, None], 4, 1, [1,2,3,4]))
#print(densityOrder(4, [2,4,1,6], [4,5,3,9]))
'''
a1 = [None, None, None, None]
a2 = 0
for i in range(32):
    a1, a2 = bypass(a1, a2)
    print(a1, a2)'''
