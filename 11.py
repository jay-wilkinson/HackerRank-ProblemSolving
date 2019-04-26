#!/usr/bin/python3
# Time Conversion

import os
import sys

s = "12:05:45PM"
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == "AM" and s[:2] == "12":
        s = s[:8]
        s = '00' + s[2:]
        return(s)
    if s[-2:] == "PM" and s[:2] == "12":
        s = s[:8]
        return(s)
    elif s[-2:] == "PM":
        s = s[:8]
        x = (int(s[:2]) + 12)
        s = str(x) + s[2:]
        return(s)
    else:
        s = s[:8]
        return(s)


result = timeConversion(s)
print(result)
