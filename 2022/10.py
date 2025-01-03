import sys
X = 1
c = 0
q = []
crt = []
fans= 0
for i in range(6):
    q.append(20+i*40)
    crt.append([])
def plot():
    r = c // 40
    if abs(c%40 - X) <= 1:
        crt[r].append('#')
    else:
        crt[r].append('.')

for line in sys.stdin:
    l = line.strip().split()
    dx = 0
    if len(l) == 1:
        # noop
        plot()
        c += 1
    elif len(l) == 0:
        break
    else:
        # addx
        dx = int(l[1])
        plot()
        c += 1
        plot()
        c += 1
    if len(q) > 0 and c >= q[0]:
        sl = q.pop(0)
        fans += sl * X
        #print(sl, X, sl* X)
    X += dx
print(fans)

for l in crt:
    print(''.join(l))