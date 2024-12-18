import sys

csize= 71
rsize = 71
fc = 1024




cmap = []
i = 0
for line in sys.stdin:
    v = line.strip().split(',')
    cmap.append((int(v[1]), int(v[0])))


def calc(fc):
    map = []
    for i in range(rsize):
        map.append([0]*csize)
    for i in range(fc):
        map[cmap[i][0]][cmap[i][1]] = 1

    vmap = []
    for i in range(rsize):
        vmap.append([0]*csize)
    vmap[0][0] = 1
    stk = [(0, 0, 1)]
    while stk:
        p = stk.pop()
        for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = p[0] + d[0]
            nc = p[1] + d[1]
            if 0 <= nr < len(vmap) and 0 <= nc < len(vmap[0]) and\
                map[nr][nc] == 0 and (vmap[nr][nc] == 0 or vmap[nr][nc] > p[2] + 1):
                vmap[nr][nc] = p[2] + 1
                stk.append((nr, nc, p[2] + 1))
    return (vmap[-1][-1] - 1)

print(calc(fc))
s = fc
e = len(cmap) - 1

while e-s != 1:
    if calc((e + s)//2) == -1:
        e = (e + s)//2
    else:
        s = (e + s)//2
print(f'{cmap[s][1]},{cmap[s][0]}')








