import sys

fans1, fans2 = 0, 0
map = []
for line in sys.stdin:
    map.append(line.strip())

node_map = {
    '#':[],
    '.':[(-1, 0), (0, 1), (1, 0), (0, -1)],
    '>':[(0, 1)],
    '<':[(0, -1)],
    'v':[(1, 0)],
    '^':[(-1, 0)]
}

sr, sc = 0, map[0].index('.')
er, ec = len(map) - 1, map[-1].index('.')
joint ={}
def count_d(r, c):
    count = 0
    if map[r][c] == '#':
        return 0
    if r==er and c==ec:
        return 4
    for d in node_map['.']:
        nr = r + d[0]
        nc = c + d[1]
        if 0 > nr:
            continue
        if nr >= len(map):
            continue
        if map[nr][nc] != '#':
            count += 1
    return count

jc = 1
joint[(sr, sc)] = 1
for i in range(len(map)):
    for j in range(len(map[0])):
        if count_d(i, j) > 2:
            joint[(i, j)] = 1 << jc
            jc += 1

def count(slope_enabled=True):
    res = []

    stack = [(sr, sc, 0, 0, (1, 0))]
    while stack:
        n = stack.pop()
        if n[0] == er and n[1] == ec:
            res.append(n[2])
            #print(n[2])
            continue
        nr = n[0]
        nc = n[1]
        nv = n[2]
        nn = n[3]
        nn = nn | joint[nr, nc]

        for d in node_map[map[nr][nc]] if slope_enabled else [n[4], (n[4][1], -n[4][0]), (-n[4][1], n[4][0])]:
            tr = nr + d[0]
            tc = nc + d[1]
            tv = nv + 1
            ld = (d[0], d[1])
            if map[tr][tc] == '#':
                continue

            while (tr, tc) not in joint:
                for td in node_map[map[tr][tc]] if slope_enabled else [ld, (-ld[1], ld[0]), (ld[1], -ld[0])]:
                    if map[tr + td[0]][tc + td[1]] == '#':
                        continue
                    tr = tr + td[0]
                    tc = tc + td[1]
                    tv += 1
                    ld = td
                    break

            #(tr, tc) in joint:
            if (joint[(tr, tc)] & nn) == 0:
                stack.append((tr, tc, tv, nn, ld))
            else:
                continue

    return max(res)


print(count(True), count(False))


