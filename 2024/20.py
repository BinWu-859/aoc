import sys

map = []
vmap = []

sr, sc = 0, 0
er, ec = 0, 0

for i,line in enumerate(sys.stdin):
    l = line.strip()

    tsc = l.find('S')
    if tsc > 0:
        sc = tsc
        sr = i
    tsc = l.find('E')
    if tsc > 0:
        ec = tsc
        er = i
    nl = [i for i in l ]
    map.append(nl)
    vmap.append([-1]*len(l))


d_map = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def get_d(r, c, ld):
    ret = []
    for d in d_map:
        if ld[0] + d[0] == 0 and ld[1] + d[1] == 0:
            continue
        nr = r + d[0]
        nc = c + d[1]
        if 0 > nr:
            continue
        if nr >= len(map):
            continue
        if map[nr][nc] != '#':
            ret.append(d)
    return ret

# Construct depth value map
stk = [(sr, sc, 0, (0, 0))]
while stk:
    p = stk.pop()
    if vmap[p[0]][p[1]] == -1 or p[2] < vmap[p[0]][p[1]]:
        vmap[p[0]][p[1]] = p[2]

    d = get_d(p[0], p[1], p[3])
    #print(p, d)
    for i in d:
        stk.append((p[0] + i[0], p[1] + i[1], p[2] + 1, i))


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def cheat(max, crit):
    sdict = {}
    ans = 0

    for i in range(len(vmap)):
        for j in range(len(vmap[0])):
            if vmap[i][j] == -1:
                continue
            for k in range(i - max, i + max + 1):
                for l in range(j - max, j + max + 1):
                    if 0 <= k < len(map) and 0 <= l < len(map[0]):
                        if vmap[k][l] != -1:
                            d = distance((k, l), (i, j))
                            if d <= max:
                                res = abs(vmap[i][j] - vmap[k][l]) - d

                                if res not in sdict:
                                    sdict[res] = 1
                                else:
                                    sdict[res] += 1
    for k in sdict:
        if k >= crit:
            ans += sdict[k]//2 # every cheat will be counted twice
    return ans

print(cheat(2, 100), cheat(20, 100))






