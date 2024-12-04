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
        if l[0][0] != 0:
            ox += l[0][0] * l[1]
            xr.append(ox)
        else:
            oy += l[0][1] * l[1]
            yr.append(oy)
    xr = list(set(xr))
    yr = list(set(yr))
    xr.sort()
    yr.sort()
    startr = 2 * xr.index(0)
    startc = 2 * yr.index(0)

    rows = 2 * len(xr) - 1
    cols = 2 * len(yr) - 1

    #print(xr, yr, startc, startr, rows, cols)

    ground = []
    for i in range(rows):
        ground.append([0]*cols)


    ground[startr][startc] = 1
    for l in op:
        dist = l[1]
        # Expand the ground table with distance between two nodes
        while dist > 0:
            delta = abs(xr[startr//2] - xr[startr//2 + l[0][0]]) + abs(yr[startc//2] - yr[startc//2 + l[0][1]])
            dist -= delta
            ground[startr + l[0][0]][startc + l[0][1]] = delta
            ground[startr + 2 * l[0][0]][startc + 2 * l[0][1]] = 1
            startr += l[0][0] * 2
            startc += l[0][1] * 2

    # Flooding from the edge nodes
    # for example part1
    # [ 1,  1,  1,  1,  1,  2,  1,  2,  1]
    # [ 2,  0,  0,  0,  0,  0,  0,  0,  2] <- distance row
    # [ 1,  1,  1,  1,  1,  0,  0,  0,  1]
    # [-1, -1, -1, -1,  3,  0,  0,  0,  3] <- distance row
    # [ 1,  1,  1,  1,  1,  0,  1,  2,  1]
    # [ 2,  0,  0,  0,  0,  0,  2, -1, -1] <- distance row
    # [ 1,  1,  1,  0,  0,  0,  1,  2,  1]
    # [-1, -1,  2,  0,  0,  0,  0,  0,  2] <- distance row
    # [-1, -1,  1,  1,  1,  2,  1,  2,  1]
    #       |       |       |       | distance col
    # for example part2
    # [1,       5411,   1,      456526, 1,      -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1]
    # [56407,   0,      0,      0,      56407,  -1,     -1,     -1,     -1,     -1,     -1,     -1,     -1]
    # [1,       0,      0,      0,      1,      35119,  1,      112010, 1,      209542, 1,      -1,     -1]
    # [299946,  0,      0,      0,      0,      0,      0,      0,      0,      0,      299946, -1,     -1]
    # [1,       0,      0,      0,      0,      0,      1,      112010, 1,      0,      1,      -1,     -1]
    # [143901,  0,      0,      0,      0,      0,      143901, -1,     143901, 0,      143901, -1,     -1]
    # [1,       5411,   1,      0,      0,      0,      1,      -1,     1,      0,      1,      -1,     -1]
    # [-1,      -1,     419393, 0,      0,      0,      419393, -1,     419393, 0,      419393, -1,     -1]
    # [-1,      -1,     1,      0,      0,      0,      1,      -1,     1,      0,      1,      367720, 1]
    # [-1,      -1,     266681, 0,      0,      0,      266681, -1,     266681, 0,      0,      0,      266681]
    # [-1,      -1,     1,      456526, 1,      35119,  1,      -1,     1,      209542, 1,      367720, 1]
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

    while high:
        pos = high.pop()
        if ground[pos[0]][pos[1]] == 0:
            ground[pos[0]][pos[1]] = -1
            if pos[0] > 0:
                high.append((pos[0] - 1, pos[1]))
            if pos[1] > 0:
                high.append((pos[0], pos[1] - 1))
            if pos[0] < rows - 1:
                high.append((pos[0] + 1, pos[1]))
            if pos[1] < cols - 1:
                high.append((pos[0], pos[1] + 1))

    for r, l in enumerate(ground):
        print(l)
        for c, g in enumerate(l):
            if g == -1:
                cv = 1 if c%2 == 0 else yr[c//2 + 1] - yr[c//2] - 1
                rv = 1 if r%2 == 0 else xr[r//2 + 1] - xr[r//2] - 1
                ans += cv*rv
    ans = (xr[-1] - xr[0] + 1) * (yr[-1] - yr[0] + 1) - ans
    return ans

print(calc(op), calc(op2))
