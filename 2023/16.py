import sys

def get_step(map, r, c, d):
    if d == 0:
        if r <= 0:
            return None
        return (r - 1, c, 3 - d)
    if d == 1:
        if c <= 0:
            return None
        return (r, c -1, 3 - d)
    if d == 2:
        if c >= len(map[0]) - 1:
            return None
        return (r, c + 1, 3 - d)
    if d == 3:
        if r >= len(map) - 1:
            return None
        return (r + 1, c, 3 - d)


def beam(map, res, r, c, d):
    road = []

    road.append((r, c, d))

    while len(road):
        r, c, d = road.pop()
        #print( r, c, d )
        if (res[r][c] // 10**(3-d))%10 == 1:
            continue
        res[r][c] += 10**(3-d)
        for nd in router_map[map[r][c]][d]:
            step = get_step(m, r, c, nd)
            #print('->',nd, '|: ', step)
            if step:
                road.append(step)
def clean_res(res):
    l = len(res[0])
    for i in range(0, len(res)):
        res[i] = [0]*len(line)

fans1 = 0
fans2 = []

#   0
# 1   2
#   3
router_map = {
   '.': ([3], [2], [1], [0]),
   '|': ([3], [0, 3], [0, 3], [0]),
   '-': ([1, 2], [2], [1], [1 ,2]),
   '\\': ([2], [3], [0], [1]),
   '/': ([1], [0], [3], [2])
}
m = []
res = []
for line in sys.stdin:
   l = line.strip()
   m.append(l)
   res.append([0]*len(line))


beam(m, res, 0, 0, 1)
fans1 = sum([sum(map(lambda x: 1 if x > 0 else 0, r)) for r in res])
clean_res(res)

for i in range(0, len(m)):
    beam(m, res, i, 0, 1)
    ans = sum([sum(map(lambda x: 1 if x > 0 else 0, r)) for r in res])
    fans2.append(ans)
    clean_res(res)

    beam(m, res, i, len(m[0]) - 1, 2)
    ans = sum([sum(map(lambda x: 1 if x > 0 else 0, r)) for r in res])
    fans2.append(ans)
    clean_res(res)

for i in range(0, len(m[0])):
    beam(m, res, 0, i, 0)
    ans = sum([sum(map(lambda x: 1 if x > 0 else 0, r)) for r in res])
    fans2.append(ans)
    clean_res(res)


    beam(m, res, len(m) - 1, i, 3)
    ans = sum([sum(map(lambda x: 1 if x > 0 else 0, r)) for r in res])
    fans2.append(ans)
    clean_res(res)


print(fans1, max(fans2))

