#!/usr/bin/python3
# Kangaroo

import math
import os
import random
import re
import sys

x1 = 0
v1 = 3
x2 = 4
v2 = 2

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    y1 = x1
    y2 = x2
    if x1 > x2 and v1 > v2:
        return("NO")
    elif x2 > x1 and v2 > v1:
        return("NO")
    elif x1 == x2 and v1 != v2:
        return("NO")
    elif v1 == v2 and v1 != v2:
        return("NO")
    else:
        for i in range(0, 10000):
            y1 += v1
            y2 += v2
            print ("Running: ", y1, y2)
            if y1 == y2:
                return("YES")
        return("NO")

# x1 = roo 1 start
# v1 = roo 1 distance
# x2 = roo 2 start
# v2 = roo 2 distance

result = kangaroo(x1, v1, x2, v2)
print(result)
