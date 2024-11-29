import sys
from heapq import heappush, heappop
#   0
# 1   2
#   3
offset = [(1, 0), (0, 1), (0, -1), (-1, 0)]
def ans01(mt, vt, min_len, max_step):
    stack = [(0, (0, 0), (0, 0)), (0, (0, 0), (1, 0))]

    while len(stack) > 0:
        v, p, h = heappop(stack)
        if p[0] < 0 or p[0] > len(mt) - 1:
            continue
        if p[1] < 0 or p[1] > len(mt[0]) -1:
            continue
        if h[1] > max_step:
            continue

        key = (p, h)
        if key in vt and v + mt[p[0]][p[1]] >= vt[key]:
            continue
        vt[key] = v + mt[p[0]][p[1]]
        #print('set', p, v ,'+', mt[p[0]][p[1]], '=', vt[key], key)
        for d in (0, 1, 2, 3):
            if d == 3 - h[0]:
                continue
            if d != h[0] and h[1] < min_len:
                continue
            dr, dc = offset[d]
            sr, sc = p[0], p[1]
            nv = vt[key]
            for i in range(0, 1):
                sr += dr
                sc += dc
                if sr < 0 or sr > len(mt) - 1:
                    break
                if sc < 0 or sc > len(mt[0]) -1:
                    break
                np = (sr, sc)
                nh = (d, h[1] + i + 1 if h[0] == d else i + 1)

                if nh[1] > max_step:
                    break

                heappush(stack, (nv, np, nh))
                #print((v, p, h),'->', (nv, np, nh))
                nv += mt[sr][sc]

fans1 = []
fans2 = []

mt = []
vt = {}
for line in sys.stdin:
    l = line.strip()
    mt.append([int(i) for i in l])
ans01(mt, vt, 0, 3)

for k in vt:
    if k[0] == (len(mt) - 1, len(mt[0]) - 1):
        fans1.append(vt[k])

vt = {}
ans01(mt, vt, 4, 10)

for k in vt:
    if k[0] == (len(mt) - 1, len(mt[0]) - 1) and k[1][1] >= 4:
        fans2.append(vt[k])

print(min(fans1) - mt[0][0], min(fans2) - mt[0][0])

