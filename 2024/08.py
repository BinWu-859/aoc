import sys

fans1, fans2 = 0, 0
grid=[]
raw=[]
band = {}

for r, line in enumerate(sys.stdin):
    l = [c for c in line.strip()]
    for c,ch in enumerate(l):
        if ch != '.':
            if ch not in band:
                band[ch] = [(r, c)]
            else:
                band[ch].append((r, c))
    raw.append(line.strip())
    grid.append(l)
def inrange(c):
    if 0 > c[0] or c[0] >= len(grid):
        return False
    if 0 > c[1] or c[1] >= len(grid[0]):
        return False
    return True

def verify(c):
    if not inrange(c):
        return False
    if grid[c[0]][c[1]] != '#':
        grid[c[0]][c[1]] = '#'
        return True
    return False
for b in band:
    for i, co in enumerate(band[b]):
        for j in range(i+1, len(band[b])):
            i1 = (2 * co[0] - band[b][j][0], 2*co[1] - band[b][j][1])
            i2 = (2 * band[b][j][0] - co[0], 2*band[b][j][1] - co[1])
            if verify(i1):
                fans1 += 1
            if verify(i2):
                fans1 += 1
grid = []
for i in raw:
    grid.append([c for c in i])

for b in band:
    for i, co in enumerate(band[b]):
        for j in range(i+1, len(band[b])):
            i = 0
            while True:
                i1 = (co[0] + i*(co[0] - band[b][j][0]), co[1] + i*(co[1] - band[b][j][1]))
                verify(i1)
                i += 1
                if not inrange(i1):
                    break

            i = 0
            while True:
                i2 = (band[b][j][0] + i*(band[b][j][0] - co[0]), band[b][j][1] + i*(band[b][j][1] - co[1]))
                verify(i2)
                i += 1
                if not inrange(i2):
                    break
print(fans1, sum([i.count('#') for i in grid]))
