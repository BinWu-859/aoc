import sys


range = []
merged_range = []
ing = []

for line in sys.stdin:
    l = line.strip()
    if l =='':
        break
    range.append(tuple(map(int, l.split('-'))))

for line in sys.stdin:
    ing.append(int(line.strip()))

range.sort(key = lambda x: x[0])
for r in range:
    if len(merged_range) == 0 or r[0] > merged_range[-1][1]:
        merged_range.append(r)
    else:
        merged_range[-1] = (merged_range[-1][0], max(merged_range[-1][1], r[1]))

# part1
ans = 0
for i in ing:
    for r in merged_range:
        if r[0] <= i <= r[1]:
            ans += 1
            break
print(ans)

# part2
ans = 0
for r in merged_range:
    ans += r[1] - r[0] + 1

print(ans)


