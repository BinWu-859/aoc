import sys

fans1, fans2 = 0, 0

cmap = {'#':0, '.':1, 'S':2}
gmap=[]

sx, sy = 0, 0
for c, line in enumerate(sys.stdin):
    l = []
    for i, ch in enumerate(line.strip()):
        l.append(cmap[ch])
        if ch == 'S':
            sx = c
            sy = i
    gmap.append(l)

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def can_stand(op, rec):
    p = [op[0], op[1]]
    if rec:
        p[0] = p[0]%len(gmap)
        p[1] = p[1]%len(gmap[0])
    if p[0] < 0 or p[0] >= len(gmap):
        return False
    if p[1] < 0 or p[1] >= len(gmap[0]):
        return False
    if gmap[p[0]][p[1]] > 0:
        return True

def run(n):
    footprint = [(sx, sy)]
    nextpos = []
    for i in range(n):
        for f in footprint:
            for s in d:
                if can_stand((f[0]+ s[0], f[1] + s[1]), False):
                    nextpos.append((f[0]+ s[0], f[1] + s[1]))

        footprint = list(set(nextpos))
        nextpos = []
    return len(footprint)

def get_co():
    a = 0
    b = 0
    n = len(gmap) * 2 + len(gmap) // 2
    val = []

    footprint = [(sx, sy)]
    nextpos = []
    for i in range(n):
        for f in footprint:
            for s in d:
                if can_stand((f[0]+ s[0], f[1] + s[1]), True):
                    nextpos.append((f[0]+ s[0], f[1] + s[1]))

        footprint = list(set(nextpos))
        nextpos = []
        if (i+1) % len(gmap) == 65:
            val.append(len(footprint))
    a = (val[2] - val[1]) - (val[1] - val[0])
    b = (val[1] - val[0]) - a

    return a, b, val[0]
#Part2:636391426712747
# 26501365=202300*131+65,
# for x in pattern p(n) = 131n+65
# run(p(k+1)) - run(p(k)) = ak + b

'''
64 3947    +31206 -> 31100*1+106
195 35153  +62306 -> 31100*2+106
326 97459  +93406 -> 31100*3+106
457 190865
'''
k = 26501365//len(gmap)
a, b, v0 = get_co()
print(a, b, v0)
print(run(64), v0 + k*b + k*(k+1)//2*a )

