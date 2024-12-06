import sys

fans1, fans2 = 0, 0

cmap = {'.':0, '#':1, '^':2}
gmap=[]
dmap=[]

sx, sy = 0, 0
for c, line in enumerate(sys.stdin):
    l = []
    for i, ch in enumerate(line.strip()):
        l.append(cmap[ch])
        if ch == '^':
            sx = c
            sy = i
    dmap.append([0]*len(l))
    gmap.append(l)


# (-1, 0) -> (0, 1) -> (1, 0) -> (0, -1)
def turnright(p):
    return (p[1], -p[0])
def getdvalue(d):
    return (d[0] + 1) * 2 +(d[1] + 1)

def walk(t = (-1, -1)):
    d = (-1, 0)
    s = [sx, sy]

    di = {}
    while True:
        if (s[0], s[1]) in di and di[(s[0], s[1])] == getdvalue(d):
            return False, 0
        di[(s[0], s[1])] = getdvalue(d)
        if s[0] + d[0] < 0 or s[0] + d[0] >= len(gmap):
            break
        if s[1] + d[1] < 0 or s[1] + d[1] >= len(gmap[0]):
            break
        # Stuck when "if"  is used
        # The following situation need a "while"
        # ...#...
        # ...^#
        while gmap[s[0] + d[0]][s[1] + d[1]] == 1 or (s[0] + d[0] == t[0] and s[1] + d[1] == t[1]):
            d = turnright(d)
        s[0] += d[0]
        s[1] += d[1]
    return True, [k for k in di]

_, tlist = walk()

for t in tlist:
    r, _ = walk(t)
    if not r:
        fans2 += 1

print(len(tlist), fans2)

