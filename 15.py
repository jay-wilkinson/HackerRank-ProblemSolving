#!/usr/bin/python3
# Day of the Programmer

import math
import os
import random
import re
import sys

year = 1920

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year < 1918:
        if year % 4 == 0:
            return("12.09." + str(year))
        else:
            return("13.09." + str(year))
    elif year > 1918:
        if year % 400 == 0:
            return("12.09." + str(year))
        elif year % 4 == 0 and year % 100 != 0 :
            return("12.09." + str(year))
        else:
            return("13.09." + str(year))
    elif year == 1918:
        return("26.09.1918")


result = dayOfProgrammer(year)
print(result)
