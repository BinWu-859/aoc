import sys

fans1 = 0
fans2 = 0

def accept(d, func):
    cur = func['in']
    while cur:
        nxt = None
        for op in cur:
            if d[op[0]] <= op[1]:
                nxt = op[2]
            else:
                nxt = op[3]
            if not nxt:
                continue
            if nxt == 'A':
                return True
            if nxt == 'R':
                return False
            cur = func[nxt]
            break

def count(func):
    ret = 0
    stack = [{'x':(1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000), 'func':'in'}]

    while stack:
        d = stack.pop()
        print(d)
        if d['func'] == 'A':
            ret += (d['x'][1] - d['x'][0] + 1) * (d['m'][1] - d['m'][0] + 1) * (d['a'][1] - d['a'][0] + 1) * (d['s'][1] - d['s'][0] + 1)
            continue
        if d['func'] == 'R':
            continue
        for i in func[d['func']]:
            if d[i[0]][0] <= i[1] < d[i[0]][1]:
                delse = d.copy()
                if not i[2]:
                    delse[i[0]] = (i[1] + 1, d[i[0]][1])
                    delse['func'] = i[3]
                    d[i[0]] = (d[i[0]][0], i[1])
                    stack.append(delse)
                    continue
                if not i[3]:
                    delse[i[0]] = (d[i[0]][0], i[1])
                    delse['func'] = i[2]
                    d[i[0]] = (i[1] + 1, d[i[0]][1])
                    stack.append(delse)
                    continue
                delse[i[0]] = (i[1] + 1, d[i[0]][1])
                delse['func'] = i[3]
                d[i[0]] = (d[i[0]][0], i[1])
                d['func'] = i[2]
                stack.append(d)
                stack.append(delse)
            else:
                if i[1] < d[i[0]][0] and i[3]:
                    d['func'] = i[3]
                    stack.append(d)
                if d[i[0]][1] <= i[1] and i[2]:
                    d['func'] = i[2]
                    stack.append(d)
    return ret
# target, critira, <= func, > func
# None A R special func
func = {}


for line in sys.stdin:
    l = line.strip().split('{')
    if len(l) < 2:
        break
    fname = l[0]
    ops = []
    rops = l[1][:-1].split(',')

    for i, s in enumerate(rops[:-1]):
        op = s.split(':')
        target = op[0][0:1]
        cp = op[0][1:2]
        val = int(op[0][2:])
        elsef = None
        if i == len(rops) - 2:
            elsef = rops[-1]
        if cp == '<':
            s = (target, val - 1, op[1], elsef)
        else:
            s = (target, val, elsef, op[1])

        ops.append(s)
    func[fname] = ops

for line in sys.stdin:
    d = {}
    v = line.strip()[1:-1].split(',')
    for i in v:
        t = i.split('=')
        d[t[0]] = int(t[1])
    if accept(d, func):
        fans1 += sum([d[k] for k in d])
fans2 = count(func)
print(fans1, fans2)