import sys

dir ={'/':{}}

d_stk = []
for line in sys.stdin:
    l = line.strip()
    if l[0] == '$':
        cmd = l[2:].split()
        if cmd[0] == 'cd':
            if cmd[1] != '..':
                d_stk.append(cmd[1])
            else:
                d_stk.pop()
            continue
        if cmd[0] == 'ls':
            cur = '/'.join(d_stk)
            continue
    f = l.split()
    if f[0] == 'dir' and f[1] not in dir:
        nd = '/'.join([cur, f[1]])
        dir[nd] = {}
        dir[cur][nd] = 0
    else:
        dir[cur][f[1]] = int(f[0])

d_size = {}
d_stk = ['/']
while d_stk:
    d = d_stk[-1]
    ts = 0
    done = True
    for f in dir[d]:
        if dir[d][f] == 0:
            if f not in d_size:
                d_stk.append(f)
                done = False
                break
            ts += d_size[f]
        else:
            ts += dir[d][f]
    if not done:
        continue
    d_size[d] = ts
    d_stk.pop()

fans1 = 0
for d in d_size:
    if d_size[d] < 100000:
        fans1 += d_size[d]
print(fans1)
print(min(list(filter(lambda i: i >= d_size['/'] - 40000000, d_size.values()))))





