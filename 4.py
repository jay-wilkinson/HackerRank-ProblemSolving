#!/usr/bin/python3

n = 6
arr = [-4, 3, -9, 0, 4, 1]

# Complete the aVeryBigSum function below.
# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0
    nx = 0
    z = 0
    for i in range(0, n):
        if arr[i] == 0:
            z += 1
        elif arr[i] < 0:
            nx += 1
        else:
            p += 1
    print('{:-f}'.format(p/n))
    print('{:-f}'.format(nx/n))
    print('{:-f}'.format(z/n))
return



print(plusMinus(arr))
