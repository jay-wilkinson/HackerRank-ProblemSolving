#!/usr/bin/python3
from random import randint

arr= [0]
for _ in range(5):
    arr.append(randint(1, 10**9))

#arr = [1, 2, 3, 4, 5]
# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
    sums = [0]
    sums[0] = arr[1] + arr[2] + arr[3] + arr[4]
    a = arr[0] + arr[2] + arr[3] + arr[4]
    b = arr[0] + arr[1] + arr[3] + arr[4]
    c = arr[0] + arr[1] + arr[2] + arr[4]
    d = arr[0] + arr[1] + arr[2] + arr[3]
    sums.append(a)
    sums.append(b)
    sums.append(c)
    sums.append(d)
    print(min(sums), max(sums))


if __name__ == '__main__':
#    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
