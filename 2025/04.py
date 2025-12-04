import sys

s_map = [(-1, 0), (-1, -1), (-1, 1),
         (0, -1), (0, 1),
         (1, -1), (1, 0), (1, 1)]

def count_paper(map, r, c):
    count = 0
    for s in s_map:
        if 0 <= r + s[0] < len(map) and 0 <= c + s[1] < len(map[0]):
            if map[r + s[0]][c + s[1]] == '@':
                count += 1
    return count

def part1(map):
    ans = 0
    x = []
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == '@':
                count = count_paper(map, r, c)
                if count < 4:
                    ans += 1
                    x.append((r, c))
    return ans, x

def part2(map):
    ans = 0
    while True:
        count, to_remove= part1(map)
        if count == 0:
            break
        ans += count
        for r, c in to_remove:
            map[r][c] = '.'
    return ans

map=[]
for line in sys.stdin:
    map.append(list(line.strip()))

print(part1(map)[0])
print(part2(map))
