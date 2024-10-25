import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from QuickSort import *
import math

lengths = [i for i in range(25, 1001, 25)]
fun = []

def squared(lengths):
    for i in lengths:
        fun.append(i**2)
squared(lengths)

print(fun)