import sys
lock = []
key = []

while True:
    num = [-1, -1, -1, -1, -1]
    is_lock = False
    for i in range(7):

        l = sys.stdin.readline().strip()
        if i == 0 and l == '#####':
            is_lock = True
        for j, c in enumerate(l):
            if c == '#':
                num[j] += 1
    if is_lock:
        lock.append(num)
    else:
        key.append(num)

    if not sys.stdin.readline():
        break

fans1 = 0
for l in lock:
    for k in key:
        ol = False
        for i in range(5):
            if l[i] + k[i] > 5:
                ol = True
        if not ol:
            fans1 += 1

print(fans1)
