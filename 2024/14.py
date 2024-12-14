import sys
import numpy as np
rc = 103
cc = 101
t = 100

def sum2(m):
    #print(m)
    return sum([sum(i) for i in m])

map = []
pl = []
vl = []

for i in range(rc):
    map.append([0]*cc)
for line in sys.stdin:
    l = line.strip().split()
    p = l[0][2:].split(',')
    v = l[1][2:].split(',')
    pl.append((int(p[1]), int(p[0])))
    vl.append((int(v[1]), int(v[0])))

    fr = (int(p[1]) + t *int(v[1]))%rc
    fc = (int(p[0]) + t *int(v[0]))%cc
    map[fr][fc] +=1
m = np.array(map)


print(sum2(m[:rc//2,:cc//2]) * sum2(m[rc//2+1:,:cc//2]) *
      sum2(m[:rc//2,cc//2+1:]) * sum2(m[rc//2+1:,cc//2+1:]))

# Print out when it MAYBE an easter egg
for i in range(0, 100*t):
    mm = []
    for j in range(rc):
        mm.append(['.']*cc)
    for j in range(len(pl)):
        fr = (pl[j][0] + i * vl[j][0])%rc
        fc = (pl[j][1] + i * vl[j][1])%cc
        mm[fr][fc] = '*'
    pr = False
    for j in mm:
        c = 0
        cl = []
        for k in j:
            if k == "*":
                c +=1
            else:
                cl.append(c)
                c = 0
        if max(cl) > 6:
            pr = True
    if pr:
        print(i)
        for j in mm:
            print(('').join(j))