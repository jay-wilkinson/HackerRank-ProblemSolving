#!/usr/bin/python3

n = 5
ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    i = 0
    total = 0
    for i in range(0, n):
        total += ar[i]
    return (total)
print(aVeryBigSum(ar))
