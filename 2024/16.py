import sys
import math

map = []

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


d_map = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def d2int(d):
    return (d[0]+1)*3+d[1]+1
def tl(d):
    return (-d[0], d[1])
def tr(d):
    return (d[0], -d[1])
def is_s(d):
    return d[0]==sr and d[1]==sc
def is_e(d):
    return d[0]==er and d[1]==ec



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

# for i in map:
#     print(''.join(i))
# get ride of some one way node
ow = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '#':
            continue
        if map[i][j] == 'S':
            continue
        d = get_d(i, j, (0, 0))
        if len(d) == 1:
            ow.append((i, j, d[0]))
#print(len(ow), ow)
while ow:
    o = ow.pop()
    map[o[0]][o[1]] = '#'
    d = get_d(o[0]+o[2][0], o[1]+o[2][1], (0, 0))
    if len(d) == 1 and map[o[0]+o[2][0]][o[1]+o[2][1]] != 'S' and map[o[0]+o[2][0]][o[1]+o[2][1]] != 'E':
        ow.append((o[0]+o[2][0], o[1]+o[2][1], d[0]))

joint ={}
joint[(sr, sc)] = 1
joint[(er, ec)] = 2
jc = 3

def build_graph():
    global jc
    graph = {}
    stack = [i for i in joint.keys()]
    while stack:
        n = stack.pop()
        if is_e(n):
            continue
        #print('check ', n)
        ds = get_d(n[0], n[1], (0, 0))
        for d in ds:
            #print(n, d)
            c = 1
            nr = n[0] + d[0]
            nc = n[1] + d[1]
            ld = [d]
            if is_s((nr, nc)):
                continue
            if not is_e((nr, nc)):
                nds = get_d(nr, nc, d)
                ld = nds
                #print(n, nds, '1')
                while len(nds) == 1:
                    nr += nds[0][0]
                    nc += nds[0][1]
                    c += 1
                    if is_s((nr, nc)) or is_e((nr, nc)):
                        break
                    nds = get_d(nr, nc, nds[0])
                    if len(nds) == 1:
                        if (nds[0] != ld[0]):
                            #print('-', nds, ld)
                            c += 1000
                        ld = nds
                    #print(n, nds, '2')
                if len(nds) > 0 and (nr, nc) not in joint:
                    stack.append((nr, nc))
                    joint[(nr, nc)] = jc
                    jc += 1
            if joint[n] not in graph:
                graph[joint[n]] = {}
            if is_e((nr, nc)) or len(nds) > 0:
                if joint[(nr, nc)] not in graph[joint[n]] or\
                    graph[joint[n]][joint[(nr, nc)]][0] > c:
                    graph[joint[n]][joint[(nr, nc)]] = (c, d, ld[0])
                    #print(joint[n], '->', joint[(nr, nc)], n, (nr, nc), c, d, ld[0])
    #print(graph)
    #print(joint)
    return graph

def run():
    g = build_graph()
    stk = [(1, 0, [], (0, 1))]
    vmap = {}
    ret = []
    sset = {}
    while stk:
        n,s,p,d = stk.pop()

        if n == joint[(er, ec)]:
            if not ret or s < min(ret):
                ret.append(s)
                sset.clear()
                for i in p:
                    sset[i] = 1
            elif s == min(ret):
                for i in p:
                    sset[i] = 1
            continue
        for l in g[n]:
            e = s + g[n][l][0]
            if d != g[n][l][1]:
                e += 1000
            k = (l, g[n][l][2])
            if k not in vmap or e <= vmap[k]:
                vmap[k] = e
                # record the paths
                np = p.copy()
                np.append((n, l))
                stk.append((l, e, np, g[n][l][2]))

    ret2 = 0
    #print('sset',  sset.keys())
    dset ={}
    for i in sset:
        dset[i[0]] = 1
        dset[i[1]] = 1
        ret2 += (g[i[0]][i[1]][0] % 1000 - 1)
        #print(f'({i[0]},{i[1]})', (g[i[0]][i[1]][0] % 1000 - 1))
    ret2 += len(dset.keys())
    return min(ret), ret2
print(run())











