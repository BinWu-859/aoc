import sys
import re

fans1 = ''
fans2 = 0

crates = []

for line in sys.stdin:
    l = line.rstrip()
    llen = len(l)
    if llen == 0:
        break
    nc = llen // 4 + 1
    while len(crates) < nc:
        crates.append([])

    for i in range(nc):
        if l[i * 4 + 1] != ' ':
            crates[i].insert(0, l[i * 4 + 1])
crates2 = []
for i in crates:
    crates2.append(i.copy())

for line in sys.stdin:
    l = line.strip()
    s = re.findall(r'move (\d+) from (\d+) to (\d+)', l)[0]
    n = int(s[0])
    src = int(s[1]) - 1
    dst = int(s[2]) - 1
    stk = []
    for i in range(n):
        k = crates[src].pop()
        crates[dst].append(k)
        stk.append(crates2[src].pop())
    while stk:
        crates2[dst].append(stk.pop())

print(''.join(i[-1] for i in crates), ''.join(i[-1] for i in crates2))




