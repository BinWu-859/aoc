import sys
import numpy as np

def check(d, c):
    for i in range(1, min(c+1, d.shape[0] - c)):
        if any(d[c - i] + d[c + i]):
            #print(c, ' x at', c - i, d[c - i] + d[c + i])
            return False
    return True
def find_smudge(d, c):
    for i in range(1, min(c+1, d.shape[0] - c)):
        if sum([abs(n) for n in d[c - i] + d[c + i]]) == 1:
            #print(c, ' x at', c - i, d[c - i] + d[c + i])
            return (c - i, c + i)
    return ()

def de_smudge(m, c, i, j):
    t = m.copy()
    t[i] = t[j]
    if check(np.diff(t, axis = 0), c):
        return c + 1
    return 0


def calc_h(m, smudge):
    ans = []
    diff = np.diff(m, axis = 0)
    #find axes
    for i, ld in enumerate(diff):
        if not smudge and not any(ld):
            if check(diff, i):
                ans.append(i + 1)
                continue
        if smudge and not any(ld):
            # smudge not on axes
            s = find_smudge(diff, i)
            if s:
                ans.append(de_smudge(m, i, s[0], s[1] + 1))
                continue

        if smudge and sum([abs(n) for n in ld]) == 1:
            # smudge on axes
            ans.append(de_smudge(m, i, i, i + 1))
            continue
    return ans

world = []
m = []

for line in sys.stdin:
    l = []
    for c in line.strip():
        if c == '.':
            l.append(0)
            continue
        if c == '#':
            l.append(1)
            continue
    if l:
        m.append(l)
    else:
        world.append(np.array(m, dtype=int))
        m = []
world.append(np.array(m, dtype=int))

v1 = 0
h1 = 0
v2 = 0
h2 = 0
for i in world:
    print(i)
    t1 = sum(calc_h(i.transpose(), False))
    t2 = sum(calc_h(i, False))
    print(t1, t2)
    v1 += t1
    h1 += t2
    t1 = sum(calc_h(i.transpose(), True))
    t2 = sum(calc_h(i, True))
    print(t1, t2)
    v2 += t1
    h2 += t2

print(v1 + 100*h1, v2 + 100*h2)


