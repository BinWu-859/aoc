import sys

map = []
map2 = []
sr, sc = 0, 0

p2_map = {
    '#': '##',
    '.': '..',
    '@': '@.',
    'O': '[]'
}
for i,line in enumerate(sys.stdin):
    l = line.strip()
    #print(i, l)
    if len(l) == 0:
        break
    tsc = l.find('@')
    if tsc > 0:
        sc = tsc
        sr = i
    nl = [i for i in l.replace('@', '.')]
    map.append(nl)
    p2nl = []
    for i in nl:
        p2nl.append(p2_map[i][0])
        p2nl.append(p2_map[i][1])
    map2.append(p2nl)


ops =''
for line in sys.stdin:
    ops = ('').join([ops, line.strip()])

opd_map = {
    '^': (-1, 0),
    '<': (0, -1),
    'v': (1, 0),
    '>': (0, 1)
}
def is_in(p):
    return 0 <= p[0] < len(map) and 0 <= p[1] < len(map[0])


def peek(p, d):
    nb = 0
    nr, nc = p[0] + d[0], p[1] + d[1]
    movable = False

    while True:
        if not is_in((nr, nc)):
            break
        if map[nr][nc] == '#':
            break
        if map[nr][nc] == '.':
            movable = True
            return movable, nb
        if map[nr][nc] == 'O':
            nb += 1
            nr += d[0]
            nc += d[1]
    return movable, nb

cr = sr
cc = sc

fans1 = 0
for i in ops:
    d = opd_map[i]
    movable, nb = peek((cr, cc), opd_map[i])
    # print(i, movable, nb)
    if not movable:
        continue
    cr += d[0]
    cc += d[1]
    map[cr][cc] = '.'
    if nb > 0:
        map[cr + nb*d[0]][cc + nb*d[1]] = 'O'
    # for j, l in enumerate(map):
    #     if j == cr:
    #         nl = l.copy()
    #         nl[cc] = '@'
    #         print(nl)
    #     else:
    #         print(l)
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] == 'O':
            fans1 += r*100+c
# for i in map:
#     print(i)
print(fans1)

def move2(p, d):
    movable = False
    nr, nc = p[0], p[1]
    if d in [(-1, 0), (1, 0)]:
        cache = []
        l = [0]*len(map2[0])
        l[p[1]] = 1
        cache.append(l)
        while True:
            nr += d[0]
            la = cache[-1]
            #print(la)
            l = [0]*len(map2[0])
            for i, v in enumerate(la):
                if v == 1:
                    if map2[nr][i] == '[':
                        l[i] = 1
                        l[i + 1] = 1
                    if map2[nr][i] == ']':
                        l[i] = 1
                        l[i - 1] = 1
                    if map2[nr][i] == '#':
                        return False
            if sum(l) == 0:
                movable = True
                break
            cache.append(l)
        if movable:
            while cache:
                p = cache.pop()
                for i,v in enumerate(p):
                    if v == 1:
                        map2[nr][i] = map2[nr - d[0]][i]
                        map2[nr - d[0]][i] = '.'
                nr -= d[0]
    else:
        nb = 0
        while True:
            nc += d[1]
            if map2[nr][nc] == '#':
                return False
            if map2[nr][nc] == '.':
                movable = True
                break
            if map2[nr][nc] == '[' or map2[nr][nc] == ']':
                nb += 1

        if movable:
            s = min(nc, p[1] + 2*d[1])
            map2[nr][p[1] + d[1]] = '.'
            for i in range(nb//2):
                map2[nr][s+2*i] = '['
                map2[nr][s+2*i + 1] = ']'

    return movable

cr = sr
cc = sc*2

fans1 = 0
for i in ops:
    d = opd_map[i]
    #print('*'*9, i)
    if move2((cr, cc), opd_map[i]):
        cr += d[0]
        cc += d[1]
    # for j, l in enumerate(map2):
    #     if j == cr:
    #         nl = l.copy()
    #         nl[cc] = '@'
    #         print(''.join(nl))
    #     else:
    #         print(''.join(l))
fans2 = 0
for r in range(len(map2)):
    for c in range(len(map2[0])):
        if map2[r][c] == '[':
            fans2 += r*100+c

print(fans2)




