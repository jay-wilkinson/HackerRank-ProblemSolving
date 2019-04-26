#!/usr/bin/python3

import math
import os
import random
import re
import sys
# n = 4
# scores = [12, 24, 10, 24]
# n = 9
# scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
n = 10
scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

# Complete the breakingRecords function below.
def breakingRecords(scores):
    scoreMin = 0
    scoreMax = 0
    scoreMinCount = 0
    scoreMaxCount = 0
    for i in range(0, n):
        if i == 0:
            scoreMin = scores[i]
            scoreMax = scores[i]
        else:
            if scores[i] < scoreMin:
                scoreMin = scores[i]
                scoreMinCount += 1
            elif scores[i] > scoreMax:
                scoreMax = scores[i]
                scoreMaxCount += 1
    return(scoreMaxCount, scoreMinCount)


result = breakingRecords(scores)
print(result)
