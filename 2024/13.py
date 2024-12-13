import sys

a = ()
b = ()
fans1 = 0
fans2 = 0
for i, line in enumerate(sys.stdin):

    if i % 4 == 0:
        l = line.strip().split(': ')[1].split(', ')
        a = (int(l[0][2:]), int(l[1][2:]))
    elif i % 4 == 1:
        l = line.strip().split(': ')[1].split(', ')
        b = (int(l[0][2:]), int(l[1][2:]))
    elif i % 4 == 2:
        l = line.strip().split(': ')[1].split(', ')

        p = (int(l[0][2:]), int(l[1][2:]))
        if (p[0]*a[1] - p[1]*a[0])%(b[0]*a[1]-a[0]*b[1]) == 0 and (p[0]*b[1] - p[1]*b[0])%(a[0]*b[1]-b[0]*a[1]) == 0:
            fans1 += (p[0]*a[1] - p[1]* a[0])//(b[0]*a[1]-a[0]*b[1]) + 3 * (p[0]*b[1] - p[1]*b[0])//(a[0]*b[1]-b[0]*a[1])

        p = (int(l[0][2:]) + 10000000000000, int(l[1][2:]) + 10000000000000)
        if (p[0]*a[1] - p[1]*a[0])%(b[0]*a[1]-a[0]*b[1]) == 0 and (p[0]*b[1] - p[1]*b[0])%(a[0]*b[1]-b[0]*a[1]) == 0:
            fans2 += (p[0]*a[1] - p[1]* a[0])//(b[0]*a[1]-a[0]*b[1]) + 3 * (p[0]*b[1] - p[1]*b[0])//(a[0]*b[1]-b[0]*a[1])

print(fans1, fans2)

