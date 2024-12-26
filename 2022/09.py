import sys
import numpy as np

map={'R': (0, 1),
     'L': (0, -1),
     'U': (-1, 0),
     'D': (1, 0)
     }
ins = []
for line in sys.stdin:
    l = line.strip().split()
    d = map[l[0]]
    s = int(l[1])
    ins.append(((d[0], d[1]),s))

acc = [(0, 0)]
tr, tc = 0, 0
for i in ins:
    tr += i[0][0]*i[1]
    tc += i[0][1]*i[1]
    acc.append((tr, tc))
vr, vc = list(zip(*acc))
nr = max(vr) - min(vr) + 1
nc = max(vc) - min(vc) + 1
sr = -min(vr)
sc = -min(vc)
print('start ', sr, sc)

def get_d(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0

tmap1 = []
tmapf = []

for i in range(nr):
    tmap1.append([0]*nc)
    tmapf.append([0]*nc)
TAIL_NUM = 9
nr = [sr]*(TAIL_NUM + 1)
nc = [sc]*(TAIL_NUM + 1)
tmap1[sr][sc] = 1
tmapf[sr][sc] = 1
for i in ins:
    for j in range(i[1]):
        nr[0] += i[0][0]
        nc[0] += i[0][1]
        for k in range(1, TAIL_NUM+1):
            rd = abs(nr[k - 1] - nr[k])
            cd = abs(nc[k - 1] - nc[k])
            dr = get_d(nr[k - 1] - nr[k])
            dc = get_d(nc[k - 1] - nc[k])
            # no need to move T
            if rd <= 1 and cd <= 1:
                continue
            nr[k] += dr
            nc[k] += dc

            if k == 1:
                tmap1[nr[k]][nc[k]] = 1
            if k == TAIL_NUM:
                tmapf[nr[k]][nc[k]] = 1

print(sum([sum(i) for i in tmap1]), sum([sum(i) for i in tmapf]))

