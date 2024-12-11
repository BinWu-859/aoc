import sys

def blink(s):
    if int(s) == 0:
        return ['1']
    if len(s)%2 == 0:
        return ['{}'.format(int(s[:len(s)//2])),
                '{}'.format(int(s[len(s)//2:]))]
    return ['{}'.format(int(s)*2024)]

def add2line(l, k, v):
    if k not in l:
        l[k] = v
    else:
        l[k] += v

def blinks(start, n):
    for i in range(n):
        nline = {}
        for k in start:
            nl = blink(k)
            for j in nl:
                add2line(nline, j, start[k])
        start = nline
    return sum([start[k] for k in start])

line = sys.stdin.readline().split()
start = {}
for i in line:
    add2line(start, i, 1)

print(blinks(start, 25), blinks(start, 75))