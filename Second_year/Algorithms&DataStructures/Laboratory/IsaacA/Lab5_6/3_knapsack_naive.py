from knapsack_tests import testKnapsackCorrectness

def generateAllBooleanCombinations(numberOfItems):
    complete_combination = []
    combination = [False for _ in range(numberOfItems)]
    for _ in range(2**numberOfItems):
        for i in range(numberOfItems-1, -1, -1):
            if combination[i]:
                combination[i] = False
            else:
                combination[i] = True
                break
        complete_combination.append(combination.copy())

    return complete_combination

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
    complete_combinations = generateAllBooleanCombinations(numberOfItems)

    for combination in complete_combinations:
        choice_weight = totalSize(sizes, combination)
        if choice_weight <= capacity:
            choice_value = totalutility(utilities, combination)
            if choice_value > maxValue:
                maxValue = choice_value
                maxCombination = combination
    
    return booleanListToSet(maxCombination)

testKnapsackCorrectness("medium")

'''capacity = capacità della borsa che porta le cose
numberOfItems = numero degli items esistenti
sizes = lista con il peso di ogni item in ordine
utilites = lista con il valore di ogni item in ordine'''