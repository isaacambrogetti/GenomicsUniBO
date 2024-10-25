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

def valueOrder(numberOfItems, utilities):
    orderedUtilities = utilities.copy()
    orderedUtilities.sort(reverse = True)
    indeces = [utilities.index(i) for i in orderedUtilities]
    return indeces

def greedyKnapsack_A(capacity, numberOfItems, sizes, utilities):
    totCapacity = 0
    combination = set()
    indeces = valueOrder(numberOfItems, utilities)

    for i in range (numberOfItems):
        if totCapacity >= capacity:
            return combination
        else:
            totCapacity += sizes[indeces[i]]
            combination.add(indeces[i])

def greedyKnapsack_B(capacity, numberOfItems, sizes, utilities):
    totCapacity = 0
    combination = set()
    indeces = densityOrder(numberOfItems, sizes, utilities)[0]

    for i in range (numberOfItems):
        if totCapacity >= capacity:
            return combination
        else:
            totCapacity += sizes[indeces[i]]
            combination.add(indeces[i])

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

'''
capacity = 5.
numberOfItems = 7
sizes = [ 3.1, 1., 2., 1.85, 0.4, 0.3, 0.6 ]
utilities = [ 7., 2., 3.9, 3.7, 0.7, 0.5, 1.]
'''
capacity = 600
numberOfItems = 20
sizes = [ 92., 4., 43., 83., 84., 68., 92., 82., 6., 44.,32., 18., 56., 83., 25., 96., 70., 48., 14., 58. ]
utilities = [ 44., 46., 90., 72., 91., 40., 75., 35., 8., 54., 78., 40., 77., 15., 61., 17., 75., 29., 75., 63. ]

#testKnapsackCorrectness("large")
print(solveKnapsack(capacity, numberOfItems, sizes, utilities)) 
print(greedyKnapsack_A(capacity, numberOfItems, sizes, utilities))
print(greedyKnapsack_B(capacity, numberOfItems, sizes, utilities))