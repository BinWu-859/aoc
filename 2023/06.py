import sys


def ans01(t, d):
    count = 0
    for i in range(1, t, 1):
        if i * (t - i) > d:
            count += 1
    return count


fans1 = 1
fans2 = 0


time = []
dist = []

time2 = 0
dist2 = 0

for line in sys.stdin:
    tmp = ''
    time = [int(i) for i in line.split(':')[1].split()]
    for c in line.split(':')[1].split():
        tmp += c
    time2 = int(tmp)
    break
for line in sys.stdin:
    tmp = ''
    dist = [int(i) for i in line.split(':')[1].split()]
    for c in line.split(':')[1].split():
        tmp += c
    dist2 = int(tmp)
    break
print(time, dist, time2, dist2)

for i, t in enumerate(time):
    fans1 *= ans01(t, dist[i])

fans2 = ans01(time2, dist2)


print(fans1, fans2)

