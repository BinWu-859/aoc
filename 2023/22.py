import sys
import numpy as np

fans1, fans2 = 0, 0

brick = []
up ={}
down = {}
def append(d, k, v):
    if k not in d:
        d[k] = [v]
    elif v not in d[k]:
        d[k].append(v)

def fall(grid, brick):
    f = 0
    for i, b in enumerate(brick):
        zd = np.nonzero(grid[b[0][0]:b[1][0]+1, b[0][1]:b[1][1]+1])
        if zd[2].size == 0:
            f = 1
        else:
            f = max(zd[2]) + 1
            for n in range(zd[2].size):
                if zd[2][n] == f - 1:
                    append(up, grid[zd[0][n]+b[0][0], zd[1][n]+b[0][1], zd[2][n]], i+1)
                    append(down, i + 1, grid[zd[0][n]+b[0][0], zd[1][n]+b[0][1], zd[2][n]])

        grid[b[0][0]:b[1][0]+1, b[0][1]:b[1][1]+1, f:f+1+b[1][2]-b[0][2]] = i + 1

for line in sys.stdin:
    mx,my,mz = 0, 0 , 0
    l = line.strip().split('~')
    s = [int(i) for i in l[0].split(',')]
    e = [int(i) for i in l[1].split(',')]
    if s[2] > e[2]:
        brick.append([e, s])
    else:
        brick.append([s, e])


brick.sort(key= lambda x: x[0][2])
mx = max([max(b[0][0], b[1][0]) for b in brick]) + 1
my = max([max(b[0][1], b[1][1]) for b in brick]) + 1
mz = max([b[1][2] for b in brick]) + 1
#print(mx, my, mz)
grid = np.zeros((mx, my, mz), dtype=int)
fall(grid, brick)

dc = []
for b in down:
    if len(down[b]) == 1:
        dc.append(down[b][0])
fans1 = len(brick) - len(set(dc))

dn=[]
for i in range(len(brick)):
    dl=[i]
    for b in dl:
        if b in up:
            for u in up[b]:
                drop = True
                for d in down[u]:
                    if d not in dl:
                        drop = False
                if drop and u not in dl:
                    dl.append(u)
    dn.append(len(dl) - 1)
print(fans1, sum(dn))

