import sys
import numpy as np


fans1 = 0
fans2 = 0
left = []
right = []

def check(nl):
    nn = np.array(nl)
    d = np.diff(nn)
    d.sort()
    if d[0] * d[-1] < 0:
        return False
    if 0 < abs(d[0]) < 4 and 0 < abs(d[-1]) < 4:
        return True
    return False


for line in sys.stdin:
    n = [ int(i) for i in line.strip().split()]
    if check(n):
        fans1 += 1
        fans2 += 1
    else:
        # O(n2)
        # Optimization to O(nlogn) (caped by complexity of sort) :
        # * Skip line with multiple neg diff and pos diff(to many bad levels)
        # * Return the BadLevel candidate list after the first check
        # But O(2) is good enough for getting gold stars of the day
        for i in range(len(n)):
            t = n.copy()
            t.pop(i)
            if check(t):
                fans2 += 1
                break

print(fans1, fans2)

