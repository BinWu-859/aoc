import sys
import numpy


fans1 = 0
fans2 = 0


for line in sys.stdin:
    d =[]
    l = [int(k) for k in line.split()]
    d.append(l)

    while any(l):
        l = numpy.diff(l)
        d.append(l)
    n = 0
    for i in range(len(d)-1, 0, -1):
        n += d[i - 1][-1]
    fans1 += n
    n = 0
    for i in range(len(d)-1, 0, -1):
        n = d[i - 1][0] - n
    fans2 += n

#
print(fans1, fans2)

