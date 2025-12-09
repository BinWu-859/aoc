import sys
import numpy as np

def sign_of_number(num):
    return (num > 0) - (num < 0)

def calc_area(a,b):
    return (abs(a[1] - b[1]) + 1) * (abs(a[0] - b[0]) + 1)
map = []
cols = []
rows = []
col_d={}
row_d={}
for line in sys.stdin:
    t = line.strip().split(',')
    map.append((int(t[1]), int(t[0])))
    cols.append(int(t[0]))
    rows.append(int(t[1]))
cols = list(set(cols))
cols.sort()
rows = list(set(rows))
rows.sort()

for i, c in enumerate(cols):
    col_d[c] = i+1
for i, r in enumerate(rows):
    row_d[r] = i+1

# +2 to add padding 1 to all the edges
map2 = np.ones((len(rows) + 2, len(cols) + 2), dtype=np.int8)
for i in range(len(map)):
    last = map[i - 1]
    cur = map[i]

    if cur[0] == last[0]:
        for j in range(cur[1], last[1], sign_of_number(last[1] - cur[1])):
            if cur[0] in row_d and j in col_d:
                map2[row_d[cur[0]]][col_d[j]] = 2
    elif cur[1] == last[1]:
        for j in range(cur[0], last[0], sign_of_number(last[0] - cur[0])):
            if j in row_d and cur[1] in col_d:
                map2[row_d[j]][col_d[cur[1]]] = 2
    if cur[0] in row_d and cur[1] in col_d:
        map2[row_d[cur[0]]][col_d[cur[1]]] = 3
"""
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
=>{2: 1, 7: 2, 9: 3, 11: 4} {1: 1, 3: 2, 5: 3, 7: 4}
Collapse "spaces" between tiles to speed up calculation
..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
=>
[1 1 1 1 1 1]
[1 1 3 2 3 1]
[1 3 3 1 2 1]
[1 3 2 3 2 1]
[1 1 1 3 3 1]
[1 1 1 1 1 1]
"""

stack = [(0, 0)]
direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while len(stack) > 0:
    c = stack.pop()
    if map2[c[0]][c[1]] == 1:
        map2[c[0]][c[1]] = 0
        for d in direct:
            if 0 <= c[0] + d[0] < len(map2) and 0 <= c[1] + d[1] < len(map2[0]) and map2[c[0] + d[0]][c[1] + d[1]] == 1:
                stack.append((c[0] + d[0], c[1] + d[1]))
"""
Flooding fill from the edge to distinguish the board of the tiles
[0 0 0 0 0 0]
[0 0 3 2 3 0]
[0 3 3 1 2 0]
[0 3 2 3 2 0]
[0 0 0 3 3 0]
[0 0 0 0 0 0]

"""
max1 = 0
max2 = 0
def inside(map2, a, b):
    if map2[a[0]][b[1]] == 0:
        return False
    if map2[b[0]][a[1]] == 0:
        return False
    for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
        if map2[i][a[1]] == 0 or map2[i][b[1]] == 0:
            return False
    for j in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
        if map2[a[0]][j] == 0 or map2[b[0]][j] == 0:
            return False
    return True


for i in range(len(map) - 1):
    for j in range(i+1, len(map)):
        a = calc_area(map[i], map[j])
        if max1 < a:
            max1 = a
        if inside(map2, (row_d[map[i][0]], col_d[map[i][1]]), (row_d[map[j][0]], col_d[map[j][1]])) and max2 < a:
            max2 = a

print(max1, max2)