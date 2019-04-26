#!/usr/bin/python3
# Apple and Orange
s = 7
t = 11
a = 5
b = 15
m = 3
n = 2
apples = [-2, 2, 1]
oranges = [5, -6]

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    x = ah = oh = 0
    for i in range(0, m):
        x = a + apples[i]
        print(x)
        if x >= s and x <= t:
            ah += 1
    for i in range(0, n):
        x = b + oranges[i]
        print(x)
        if x >= s and x <= t:
            oh += 1
    print(ah)
    print(oh)
    return()

countApplesAndOranges(s, t, a, b, apples, oranges)

# s and t are house corners, a and b trees
# m and n are number of apples and oranges
# apples and oranges are where they fell. - is left + is right
# x is hit location
