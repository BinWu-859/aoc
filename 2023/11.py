import sys
import numpy as np

def ans(nm, expd):
    ans = 0
    expc = []
    for i in range(0, nm.shape[1], 1):
        if any(nm[:, i]):
            expc.append(1)
        else:
            expc.append(expd)
    expr = []
    for i in range(0, nm.shape[0], 1):
        if any(nm[i, :]):
            expr.append(1)
        else:
            expr.append(expd)
    #print(expc, expr)
    galaxy=[]
    #re-locate galaxy
    for i in range(0, nm.shape[0], 1):
        for j in range(0, nm.shape[1], 1):
            if nm[i][j] != 0:
                galaxy.append((sum(expc[:j]), sum(expr[:i])))
    #print(galaxy)

    #calc distance
    for i in range(0, len(galaxy), 1):
        for j in range(i, len(galaxy), 1):
            ans += abs(galaxy[i][0]- galaxy[j][0]) + abs(galaxy[i][1]- galaxy[j][1])
    return ans

m = []
for line in sys.stdin:
    l = []
    for c in line.strip():
        if c == '.':
            l.append(0)
            continue
        if c == '#':
            l.append(1)
            continue
    m.append(l)
nm = np.array(m)



print(ans(nm, 2), ans(nm, 1000000))


