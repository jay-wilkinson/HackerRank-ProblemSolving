#!/usr/bin/python3

import math
import os
import random
import re
import sys

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = "abc"

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    r = 1
    print(h)
    print(h[0])
    print(h[25])
    print(str.encode(word))
    for i in range(0, len(word)):
        print(i)
        x = (ord(word[i]) - 97)
        y = (h[x])
        print(r, y)
        if y >= r:
            print("Update r")
            r = y
    return(len(word) * r)


result = designerPdfViewer(h, word)
print(result)
