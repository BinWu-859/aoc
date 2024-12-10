import sys

map = []
pmap = []
dmap = []
th = []
ep = {}
epv = 1
for r, line in enumerate(sys.stdin):
    l = []
    p = []
    d = []
    for c, ch in enumerate(line.strip()):
        if ch == '.':
            l.append(-1)
        else:
            l.append(int(ch))
        p.append(0)
        d.append(0)
        if ch == '0':
            th.append((r, c))
        if ch == '9':
            ep[(r, c)] = epv
            epv = epv << 1
    map.append(l)
    pmap.append(p)
    dmap.append(d)

def within_map(c):
    return 0 <= c[0] < len(map) and 0 <= c[1] < len(map[0])

dir=[(-1, 0), (0, -1), (1, 0), (0, 1)]
for h in th:
    path = [h]
    stk = [path]
    while stk:
        p = stk.pop()
        if map[p[-1][0]][p[-1][1]] == 9:
            for d in p:
                pmap[d[0]][d[1]] = pmap[d[0]][d[1]] | ep[p[-1]]
                dmap[d[0]][d[1]] += 1
            continue
        # Speed up, reuse the calculated value in previous rounds
        if pmap[p[-1][0]][p[-1][1]] > 0:
            for d in p[:-1]:
                pmap[d[0]][d[1]] = pmap[d[0]][d[1]] | pmap[p[-1][0]][p[-1][1]]
                dmap[d[0]][d[1]] += dmap[p[-1][0]][p[-1][1]]
            continue

        for dlt in dir:
            np = (p[-1][0] + dlt[0], p[-1][1] + dlt[1])
            if not within_map(np):
                continue
            if map[np[0]][np[1]] == map[p[-1][0]][p[-1][1]] + 1:
                npt = p.copy()
                npt.append(np)
                stk.append(npt)


print(sum([pmap[i[0]][i[1]].bit_count() for i in th]),
      sum([dmap[i[0]][i[1]] for i in th]))
