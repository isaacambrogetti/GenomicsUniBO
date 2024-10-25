import random
import cProfile

global c
c = 0

def insertionSort(unsortedList: list):
    sortedList = []
    for element in unsortedList:
        insertInSortedList(sortedList, element)
    return sortedList

def insertInSortedList(sortedList: list, element: int):
    global c
    for i in range(len(sortedList)):
        c += 1
        if sortedList[i] >= element:
            sortedList.insert(i, element)
            return
    return sortedList.append(element)
    

global d
d = 0

def mergeSort(unsortedList: list):
    if len(unsortedList) <= 1:
        return unsortedList.copy()
    center = int(len(unsortedList) / 2)
    sortedList1 = mergeSort(unsortedList[:center])
    sortedList2 = mergeSort(unsortedList[center:])
    return mergeSortedLists(sortedList1, sortedList2)

def mergeSortedLists(list1: list, list2: list):
    global d
    orderedList = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            orderedList.append(list2[j])
            j += 1
        else:
            orderedList.append(list1[i])
            i += 1
        d += 1

    if i != len(list1):
        orderedList.extend(list1[i:])

    if j != len(list2):
        orderedList.extend(list2[j:])
    return orderedList


def randomIntList(dim: int):
    list = []
    for i in range(dim):
        list.append(random.randint(0, 100))
    return list


'''dimensions = [10, 100, 1000, 10000, 100000]

for dim in dimensions:
    l = randomIntList(dim)

    cProfile.run('insertionSort(l)')
    cProfile.run('mergeSort(l)')

    print(dim, c, d, '\n')
    c = 0
    d = 0'''