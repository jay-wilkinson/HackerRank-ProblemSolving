#!/usr/bin/python3

a = [17, 28, 30]
b = [99, 16, 8]

def compareTriplets(a, b):
    aa = 0
    bb = 0
    e = 0
    for e, x in enumerate(a, start=0):
        print (e)
        if a[e] > b[e]:
            aa += 1
            print ("AA =", aa)
        elif a[e] < b[e]:
            bb += 1
            print ("BB =", bb)
    return (aa, bb)


print(compareTriplets(a,b))
