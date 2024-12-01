import sys


fans1 = 0
fans2 = 0
left = []
right = []
for line in sys.stdin:
    l ,r = line.strip().split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

for i, l in enumerate(left):
    fans1 += abs(l - right[i])
m ={}
for r in right:
    if r in m:
        m[r] += 1
    else:
        m[r] = 1
for l in left:
    if l in m:
        fans2 += m[l] * l


print(left, right)
print(fans1, fans2)

