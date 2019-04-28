#!/usr/bin/python3
# Grading Students

n = 4
grades = [73, 67, 38, 33]

import os
import sys


def gradingStudents(grades):
    x = 0
    gradesMod = []
    for i in range(0, n):
        if grades[i] > 37:
            x = grades[i]
            if x % 5 > 2:
                gradesMod.append(((x // 5) + 1) * 5)
                print(grades[i])
            else:
                gradesMod.append(grades[i])
        else:
            gradesMod.append(grades[i])
    return(gradesMod)


# n = int(input()) Number of items
# grades = []
result = gradingStudents(grades)
print(result)
