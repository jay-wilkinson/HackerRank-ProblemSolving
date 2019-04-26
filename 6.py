#!/usr/bin/python3

n = 4
# Complete the staircase function below.
x = "#"
y = " "
def staircase(n):
    for i in range(0, n):
        if i == n - 1:
            print(x * (i + 1))
        else:
            print(y * (n - (i + 1)) + x * (i + 1))
        print(i)


staircase(n)
