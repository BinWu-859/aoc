import sys

map = {}

for line in sys.stdin:
    e = line.strip().split('-')
    if e[0] not in map:
        map[e[0]] = {}
    map[e[0]][e[1]] = 0
    if e[1] not in map:
        map[e[1]] = {}
    map[e[1]][e[0]] = 0

fans1 = 0
cm = {}
for i in map:
    for j in map[i]:
        for k in map[j]:
            if k in map[i]:
                l = [i, j, k]
                l.sort()
                nk = tuple(l)
                if nk not in cm:
                    cm[nk] = 't' in i[0]+j[0]+k[0]
                    if cm[nk]:
                        fans1 += 1


print(fans1)

p2m = {}
for m in cm:
    stack = [m]
    while stack:
        p = stack.pop()
        if p in p2m:
            # Speed up
            continue
        p2m[p] = len(p)
        cc = {}
        # count occurrence in common connections, new member for LAN party should
        # have the same count as the member number
        for i in p:
            for j in map[i]:
                if j not in cc:
                    cc[j] = 1
                else:
                    cc[j] += 1
        lc = len(p)
        for c in cc:
            if cc[c] == lc:
                np = list(p)
                np.append(c)
                np.sort()
                stack.append(tuple(np))

mx = max(p2m[i] for i in p2m)
k = next((k for k in p2m if p2m[k] == mx), None)
print(','.join(k))




