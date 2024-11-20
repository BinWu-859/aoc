import sys

def match(str):
    l = []
    match = 0
    card = str.split(':')[1].split('|')
    for i in card[0].split():
        l.append(int(i))
    for i in card[1].split():
        l.append(int(i))
    l.sort()
    for i, n in enumerate(l):
        if i == 0:
            continue
        if n == l[i - 1]:
            match = match + 1
    return match


def ans01(line):
    m = match(line)

    if m == 0:
        return 0
    return pow(2, m-1)

copys = []
def ans02(line):
    global copys

    m = match(line)
    if len(copys) == 0:
        c = 0
    else:
        c = copys.pop(0)


    for i in range(1, m + 1, 1):
        if len(copys) < i:
            copys.append(c + 1)
        else:
            copys[i - 1] += (c + 1)
    return c + 1


fans1 = 0
fans2 = 0
for line in sys.stdin:
    sline = line.rstrip()
    if '' == sline:
        break
    fans1 += ans01(sline)
    fans2 += ans02(sline)
print(fans1, fans2)

