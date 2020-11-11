import math

def mac_abs_val(lst):
    currentMax = 0
    previousMax = 0
    for i in lst:
        currentMax = math.fabs(i)
        if currentMax > previousMax:
            previousMax = currentMax

    return previousMax