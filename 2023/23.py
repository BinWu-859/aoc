import sys

fans1, fans2 = 0, 0
map = []
for line in sys.stdin:
    map.append(line.strip())

node_map = {
    '#':[],
    '.':[(1, 0), (-1, 0), (0, 1), (0, -1)],
    '>':[(0, 1)],
    '<':[(0, -1)],
    'v':[(1, 0)],
    '^':[(-1, 0)]
}

sr, sc = 0, map[0].index('.')
er, ec = len(map) - 1, map[-1].index('.')
joint ={}

def get_d(r, c, ld):
    ret = []
    for d in node_map[map[r][c]]:
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

jc = 1
joint[(sr, sc)] = 1

def build_graph():
    global jc
    graph = {}
    stack = [i for i in joint.keys()]
    while stack:
        n = stack.pop()
        ds = get_d(n[0], n[1], (0, 0))
        if n[0] == er and n[1] == ec:
            continue
        for d in ds:
            c = 1
            nr = n[0] + d[0]
            nc = n[1] + d[1]
            nds = get_d(nr, nc, d)
            while len(nds) == 1:
                nr += nds[0][0]
                nc += nds[0][1]
                c += 1
                nds = get_d(nr, nc, nds[0])
            if (nr, nc) not in joint:
                stack.append((nr, nc))
                joint[(nr, nc)] = 1 << jc
                jc += 1
            if joint[n] not in graph:
                graph[joint[n]] = {}
            if len(nds) > 0 or (nr == er and nc == ec):
                graph[joint[n]][joint[(nr, nc)]] = c
    return graph

def run():
    g = build_graph()
    stk = [(1, 0, 1)]
    steps = []
    while stk:
        n,s,p = stk.pop()
        if n == joint[(er, ec)]:
            steps.append(s)
            continue
        for l in g[n]:
            if l & p == 0:
                stk.append((l, s+g[n][l], l|p))
    return(max(steps))
print(run())


for i, l in enumerate(map):
    for c in '<>^v':
        l = l.replace(c, '.')
    map[i] = l
print(run())


