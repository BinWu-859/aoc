import sys
import numpy as np

def roll(m, r):
    n = []
    count0 = 0
    count1 = 0
    if r:
        k = reversed(m)
    else:
        k = m
    for i in k:
        if i == 0:
            count0 += 1
        if i == 1:
            count1 += 1
        if i == 2:
            n.extend(([1]*count1))
            n.extend([0]*count0)
            n.append(2)
            count0 = 0
            count1 = 0
    n.extend(([1]*count1))
    n.extend([0]*count0)

    for i, v in enumerate(n):
        if r:
            m[len(m) - i -1 ] = v
        else:
            m[i] = v

def calc_load(m):
    ret = 0
    ml = len(m)
    for i, v in enumerate(m):
        if v == 1:
            ret += (ml - i)
    return ret

world = []
m = []
ans1 = 0
ans2 = 0

for line in sys.stdin:
    md = {'O': 1, '#': 2, '.':0 }
    l = []
    for c in line.strip():
        if c in md:
            l.append(md[c])
    if l:
        m.append(l)

world = np.array(m, dtype=int)
for i in range(0, world.shape[1]):
    roll(world[:, i], False)
for i in range(0, world.shape[1]):
    ans1 += calc_load(world[:, i])
world = np.array(m, dtype=int)
cache={}
cycle = 1000000000
left = cycle
for t in range(0, cycle):
    for i in range(0, world.shape[1]):
        roll(world[:, i], False)
    for i in range(0, world.shape[0]):
        roll(world[i, :], False)
    for i in range(0, world.shape[1]):
        roll(world[:, i], True)
    for i in range(0, world.shape[0]):
        roll(world[i, :], True)
    tt = 0
    for i in range(0, world.shape[1]):
        tt += calc_load(world[:, i])
    #print(world, t, tt)
    key = ''.join([''.join(['{}'.format(n) for n in i]) for i in world])
    #key = '{}'.format(world)

    left -= 1
    if key in cache:
        left =  (cycle - t  - 1)%(t - cache[key])
        print('left ', left, cycle - t - 1, t, cache[key])
    else:
        cache[key] = t
        #print('insert', key, t)
    if left == 0:
        break
for i in range(0, world.shape[1]):
    ans2 += calc_load(world[:, i])


print(t, ans1, ans2)


