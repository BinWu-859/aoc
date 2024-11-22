import sys
import math

def toIndex(c):
    if c == 'R':
        return 1
    if c == 'L':
        return 0
    return 2

fans1 = 0


route = []
rmap = {}

for line in sys.stdin:
    for c in line.strip():
        i = toIndex(c)
        if i < 2:
            route.append(i)
    break
sys.stdin.readline()
for line in sys.stdin:
    line = line.strip().replace('(', '').replace(')', '').replace(' ', '')

    t = line.split('=')
    rmap[t[0]] = t[1].split(',')

#print(rmap)
s = 'AAA'
while True:
    s = rmap[s][route[fans1%len(route)]]
    fans1 += 1
    if s == 'ZZZ':
        break

fans2 = []
for i in rmap:
    if i[2] == 'A':
        tans = 0
        s = i
        while True:
            s = rmap[s][route[tans%len(route)]]
            tans += 1
            if s[2] == 'Z':
                fans2.append(tans)
                break

#print(fans2)
print(fans1, math.lcm(*fans2))

