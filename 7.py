#!/usr/bin/python3
import math

n = 50
# Complete the viralAdvertising function below.
def viralAdvertising(n):
    s = 5
    l = 0
    c = 0
    for i in range(0, n):
        l = math.floor(s / 2)
        c = c + l
        print((i + 1), s, l, c)
        s = l * 3
    return(c)
result = viralAdvertising(n)


# i = day
# s = shared
# l = liked
# c = cumulative, day 1 = l, day 2+ = l(day2) + l(day1)
