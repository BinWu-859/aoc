import sys
import math

fans1 = 0
fans2 = 0

bc = []
name_map={}
ff_r = {}
cj_r = {}
ff_st = {}
cj_st = {}

def set_default():
    for i in ff_st:
        ff_st[i] = 0
    for i in cj_st:
        for j in cj_st[i]:
            cj_st[i][j] = 0


def is_default():
    for i in ff_st:
        if ff_st[i] == 1:
            return False
    for i in cj_st:
        for j in cj_st[i]:
            if cj_st[i][j] == 1:
                return False
    return True

def press(mo_list = [], count = 0):
    c = [len(bc) + 1, 0]
    q = [(i, 0, 'br') for i in bc]
    while q:
        op = q.pop(0)

        if op[0] not in name_map:
            continue
        if name_map[op[0]] == 1:
            #ff
            if op[1] == 0:
                ff_st[op[0]] = 1 - ff_st[op[0]]
                out = ff_st[op[0]]
                c[out] += len(ff_r[op[0]])
                for n in ff_r[op[0]]:
                    q.append((n, out, op[0]))

        if name_map[op[0]] == 2:
            #cj
            out = 1
            cj_st[op[0]][op[2]] = op[1]
            if sum([cj_st[op[0]][i] for i in cj_st[op[0]]]) == len(cj_st[op[0]]):
                out = 0
            c[out] += len(cj_r[op[0]])
            if op[0] in mo_list and out == 1 and mo_list[op[0]] == 0:
                 mo_list[op[0]] = count
            for n in cj_r[op[0]]:
                q.append((n, out, op[0]))
    return c[0], c[1]



for line in sys.stdin:
    l = line.strip().split(' -> ')
    if l[0][0] == 'b':
        bc.extend(l[1].split(', '))
        continue
    if l[0][0] == '%':
        ff_r[l[0][1:]] = l[1].split(', ')
        ff_st[l[0][1:]] = 0
        name_map[l[0][1:]] = 1
        continue
    if l[0][0] == '&':
        cj_r[l[0][1:]] = l[1].split(', ')
        cj_st[l[0][1:]] = {}
        name_map[l[0][1:]] = 2
        continue
for cj in cj_st:
    for ff in ff_r:
        if ff_r[ff].count(cj) > 0:
            cj_st[cj][ff] = 0

#print(bc, ff_r, ff_st, cj_r, cj_st, name_map)

def mp(n):
    lcl = []
    hcl = []
    while True:
        lc, hc = press()
        lcl.append(lc)
        hcl.append(hc)
        if is_default():
            break
        if len(lcl) == n:
            break

    d = n//len(lcl)
    r = n%len(lcl)
    return  (d * sum(lcl) + sum(lcl[0: r])) * (d * sum(hcl) + sum(hcl[0: r]))

def cp(name):
    #Who is connected to name
    set_default()
    lcj = ''
    for i in cj_r:
        if name in cj_r[i]:
            lcj = i

    count = 0
    go = True
    v = cj_st[lcj].copy()
    while go:
        go = False
        count += 1
        press(v, count)
        for i in v:
            if v[i] == 0:
                go = True

    return math.lcm(*[v[i] for i in v])




print(mp(1000), cp('rx'))