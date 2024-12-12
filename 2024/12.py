import sys

map = []
mark = []
fans1 = 0
fans2 = 0
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def con_count(l):
    c = 1
    for i in range(len(l) - 1):
        if l[i] != l[i + 1] - 1:
            c += 1
    return c
def calc_sides(ed):
    s = 0
    tbl = {}
    for i in ed:
        if i[1] not in tbl:
            tbl[i[1]] = [i[0]]
        else:
            tbl[i[1]].append(i[0])

    for i in tbl:
        tbl[i].sort()
        s += con_count(tbl[i])
    return s

def within_map(c):
    return 0 <= c[0] < len(map) and 0 <= c[1] < len(map[0])

def render(mark, i, j, v):
    c = map[i][j]
    a = 0
    stack = [(i, j)]
    while stack:
        nc = stack.pop(0)
        if mark[nc[0]][nc[1]] != v:
            a+=1
            mark[nc[0]][nc[1]] = v
            for d in dir:
                if within_map((nc[0]+d[0], nc[1]+d[1])) and map[nc[0]+d[0]][nc[1]+d[1]] == c:
                    if mark[nc[0]+d[0]][nc[1]+d[1]] != v:
                        stack.append((nc[0]+d[0], nc[1]+d[1]))
    r = a
    p = 0
    vedge = []
    hedge = []
    for i in range(len(mark)):
        for j in range(len(mark[0])):
            if mark[i][j] == v:
                # 0.1 to differ if the fence is inside or outside
                if j == 0 or mark[i][j - 1] != v:
                    p += 1
                    vedge.append((i, j - 0.1))
                if i == 0 or mark[i - 1][j] != v:
                    p += 1
                    hedge.append((j, i- 0.1))
                if j == len(mark[0]) - 1 or mark[i][j + 1] != v:
                    p += 1
                    vedge.append((i, j + 1.1))
                if i == len(mark) - 1 or mark[i + 1][j] != v:
                    p += 1
                    hedge.append((j, i + 1.1))
                r -= 1
                if r == 0:
                    vedge = list(set(vedge))
                    hedge = list(set(hedge))
                    return a, p, calc_sides(vedge) + calc_sides(hedge)

    return None
for line in sys.stdin:
    l = line.strip()
    map.append(l)
    mark.append([0]*len(l))

cc = 1
for i in range(len(map)):
    for j in range(len(map[0])):

        if mark[i][j] == 0:
            a, p, s = render(mark, i, j, cc)
            fans1 += a*p
            fans2 += a*s
            cc+=1

print(fans1, fans2)