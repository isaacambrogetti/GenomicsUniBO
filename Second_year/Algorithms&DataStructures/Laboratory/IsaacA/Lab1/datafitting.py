import numpy
import scipy.optimize
from codetiming import Timer
from exercise import *
import math

length = 10
repetition = 100
result = []

for _ in range(repetition):
    r_input = randomIntList(length)
    with Timer(name = "insertion_sort", logger = None):
        insertionSort(r_input)
    with Timer(name = 'merge_sort', logger = None):
        mergeSort(r_input)

'''result.append(Timer.timers.mean("insertion_sort"))
result.append(Timer.timers.mean("merge_sort"))
print(result)'''

length = [0, 150, 300, 450, 600, 750, 900, 1050, 1200, 1350, 1500, 1650, 1800, 1950, 2100, 2250, 2400, 2550, 2700, 2850, 3000]
result = []
insertionTime = []
mergeTime = []

def testSortAlgs(lengths, repetitions):
    for l in lengths:
        for _ in range(repetitions):
            r_input = randomIntList(l)
            with Timer(name = "insertion_sort", logger = None):
                insertionSort(r_input)
            with Timer(name = 'merge_sort', logger = None):
                mergeSort(r_input)
        
        insertionTime.append(Timer.timers.mean("insertion_sort"))
        mergeTime.append(Timer.timers.mean("merge_sort"))
    return insertionTime, mergeTime

(insertionTime, mergeTime) = testSortAlgs(length, repetition)
result = [insertionTime, mergeTime]
print(result)

def insertionFunc(x, a, b):
    return a*x^2 + b*x^2

def mergeFunc(x, a, b):
    return a * x * math.log10(x) + b * x

scipy.optimize.curve_fit(insertionFunc, length, insertionTime)

