import sys

dims = []
counts = []
ans1 = 0
for line in sys.stdin:
    if 'x' not in line:
        continue
    l = line.strip().split(': ')
    dims.append(list(map(int, l[0].split('x'))))
    counts.append(list(map(int, l[1].split(' '))))

for i, d in enumerate(dims):
    if sum(counts[i]) <= (d[0] // 3) * (d[1] // 3):
        # Every single tile have a 3*3 box
        ans1 += 1
    elif sum(counts[i])*7 < d[0] * d[1]:
        print(i, " Need to play with")
    else:
        # the amount of '#' is more than the area, no need to look into
        pass
print(ans1, len(dims))

