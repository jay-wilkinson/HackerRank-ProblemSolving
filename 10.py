#!/usr/bin/python3
# Birthday Cake Candles

import math
import os
import random
import re
import sys

ar_count = 10
ar = [3, 2, 1, 3, 5, 5, 5, 3, 4, 2]

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max = 0
    x = 0
    for i in range(0, ar_count):
        if ar[i] > max:
            max = ar[i]
    for i in range(0, ar_count):
        if ar[i] == max:
            x += 1
    print(max)
    print(x)
    return(x)



result = birthdayCakeCandles(ar)
