import sys



def count(map, stack):
    ret = 0
    while stack:
        i, j, delta, c = stack.pop()

        if 0 <= i <= len(map) - 1 and 0 <= j <= len(map[0]) - 1:
            if c != map[i][j]:
                continue
            if c == 8:
                ret += 1
                continue
            stack.append((i + delta[0], j + delta[1], delta, c*2))
    return ret

def count2(map, stack):
    ret = 0
    while stack:
        i, j = stack.pop()
        if 0 < i < len(map) - 1 and 0 < j < len(map[0]) - 1:
            if map[i-1][j-1] + map[i+1][j+1] == 10 and map[i-1][j+1] + map[i+1][j-1] == 10:
                ret += 1
    return ret

fans1, fans2 = 0, 0

cmap = {'X':1, 'M':2, 'A':4, 'S':8}
map = []
stack = []
stack2 = []
i = 0
for line in sys.stdin:
    l = []

    for j, ch in enumerate(line.strip()):
        l.append(cmap[ch])
        if ch == 'X':
            stack.append((i + 1, j + 1, (1, 1), 2))
            stack.append((i + 1, j, (1, 0), 2))
            stack.append((i + 1, j - 1, (1, -1), 2))
            stack.append((i - 1, j + 1, (-1, 1), 2))
            stack.append((i - 1, j, (-1, 0), 2))
            stack.append((i - 1, j - 1, (-1, -1), 2))
            stack.append((i, j + 1, (0, 1), 2))
            stack.append((i, j - 1, (0, -1), 2))
        if ch == 'A':
            stack2.append((i, j))
    i += 1
    map.append(l)

print(count(map, stack), count2(map,stack2))

