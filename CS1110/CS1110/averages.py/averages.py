# Nolan Harris
# Nph2tx

import math

def mean(a, b, c):
    '''This computes the mean of a, b, and c'''
    x = (a + b + c) / 3
    y = float(x)

    print (y)


def median(a, b, c):
    '''This computes the median of a, b, and c'''

    if a <= b <= c or c <= b <= a:
           return b
    elif b <= a <= c or c <= a <= b:
            return a
    else:
            return c

def rms(a, b, c):
    '''This calculates the rms of a, b, c'''

    mean = (a ** 2) + (b ** 2) + (c ** 2)

    x = mean//3

    z = math.sqrt(x)

    print (z)

def middle_average(a, b, c):
    '''This finds the middle average of the data set'''

    x = (a + b + c) / 3
    y = float(x)

    print(y)
    














