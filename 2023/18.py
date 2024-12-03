import sys

def extract(c):
    m = {'3':(-1, 0), '2':(0, -1), '0':(0, 1), '1':(1, 0)}
    return (m[c[-2:-1]], int(c[2:-2], 16))

op = []
op2 = []
vt = {}
tw ,th = 0, 0
for line in sys.stdin:
    m = {'U':(-1, 0), 'L':(0, -1), 'R':(0, 1), 'D':(1, 0)}
    l = line.strip().split()
    op.append((m[l[0]], int(l[1])))
    op2.append(extract(l[2]))

def calc(op):
    ans = 0
    # Calculate the size of ground and start coord
    ox,oy = 0, 0
    xr = []
    yr = []
    for l in op:
        print(l)
        if l[0][0] != 0:
            ox += l[0][0] * l[1]
            xr.append(ox)
        else:
            oy += l[0][1] * l[1]
            yr.append(oy)
    minx = min(xr)
    maxx = max(xr)
    miny = min(yr)
    maxy = max(yr)
    rows = maxx - minx + 1
    cols = maxy - miny + 1
    startr = ox - minx
    startc = oy - miny

    ground = []
    for i in range(rows):
        ground.append([0]*cols)

    ground[startr][startc] = 1
    for l in op:
        for i in range(l[1]):
            ground[startr + l[0][0] * i][startc + l[0][1] * i] = 1
        startr += l[0][0] * l[1]
        startc += l[0][1] * l[1]

    high = []
    for i in range(rows):
        if ground[i][0] == 0:
            high.append((i, 0))
        if ground[i][cols - 1] == 0:
            high.append((i, cols - 1))
    for i in range(cols):
        if ground[0][i] == 0:
            high.append((0, i))
        if ground[rows - 1][i] == 0:
            high.append((rows - 1, i))
    for i in ground:
        print(i)

    while high:
        pos = high.pop()
        if ground[pos[0]][pos[1]] == 0:
            ground[pos[0]][pos[1]] = 2
            if pos[0] > 0:
                high.append((pos[0] - 1, pos[1]))
            if pos[1] > 0:
                high.append((pos[0], pos[1] - 1))
            if pos[0] < rows - 1:
                high.append((pos[0] + 1, pos[1]))
            if pos[1] < cols - 1:
                high.append((pos[0], pos[1] + 1))

    for l in ground:
        for i in l:
            if i == 2:
                ans += 1

    ans = cols * rows - ans
    return ans


print(calc(op), calc(op2))
