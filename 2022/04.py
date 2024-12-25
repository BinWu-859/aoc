import sys
import math

fans1 = 0
fans2 = 0

for l in sys.stdin:
    ins=[0, 0]
    line = l.strip().split(',')
    left = [int(t) for t in line[0].split('-')]
    right = [int(t) for t in line[1].split('-')]

    ins[0] = max(left[0], right[0])
    ins[1] = min(left[1], right[1])

    if ins[0] == left[0] and ins[1] == left[1]:
        fans1 += 1
    elif ins[0] == right[0] and ins[1] == right[1]:
        fans1 += 1

    if ins[0] <= ins[1]:
        fans2 += 1

print(fans1, fans2)




