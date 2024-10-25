from QuickSort import *
from codetiming import Timer
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def testAlreadySortedL(L, repetition):
    for l in lengths:
        for _ in range(repetition):
            L = randomIntList(l, 500)
            quickSort(L, 0, len(L)-1)
            with Timer(name = "AlreadySortedQS", logger = None):
                quickSort(L, 0, len(L)-1)
        quickSortTimeSorted.append(Timer.timers.mean("AlreadySortedQS"))

def testSortAlgs(lengths, repetition):
    for l in lengths:
        for _ in range(repetition):
            L = randomIntList(l, 100000)
            with Timer(name = "QuickSort", logger = None):
                quickSort(L, 0, len(L)-1)
        quickSortTime.append(Timer.timers.mean("QuickSort"))



repetition = 10                                 # 2.2 punto 1
lengths = [i for i in range(25, 1001, 25)]
quickSortTimeSorted = []

testAlreadySortedL(lengths, repetition)
print(quickSortTimeSorted)


'''repetition = 10                                 # 2.2 punto 2
lengths = [i for i in range(1000, 100000, 1000)]
quickSortTime = []

testSortAlgs(lengths, repetition)
print(quickSortTime)'''

fun = []

def squared(lengths):
    for i in lengths:
        fun.append(i**2)

squared(lengths)

plt.plot(lengths, quickSortTimeSorted, 'r')
plt.plot(lengths, fun, 'b')
plt.show()