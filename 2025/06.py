import sys
import re

def part1():
    numbers = []
    op = [] # True for +, False for *

    for line in sys.stdin:
        l = line.strip().split()
        if l[0].isdigit() == True:
            numbers.append(list(map(lambda x: int(x), l)))
        else:
            op = list(map(lambda x: x=='+', l))

    part1 = 0
    for c in range(len(numbers[0])):
        if op[c]:
            ans = 0
        else:
            ans = 1
        for r in range(len(numbers)):
            if op[c]:
                ans += numbers[r][c]
            else:
                ans *= numbers[r][c]
        #print('-', ans)
        part1 += ans
    return part1

def part2():
    part2 = 0
    lines = []
    op = [] # True for +, False for *
    opn = []


    for line in sys.stdin:
        if line[0] != '*' and line[0] != '+':
            lines.append(line)
        else:
            op = list(map(lambda x: x=='+', line.strip().split()))
    ns = []
    for c in range(len(lines[0])):
        s = ''
        for j in range(len(lines)):
            s += lines[j][c]
        s = s.strip()
        if s.isdigit():
            ns.append(int(s))
        else:
            opn.append(ns)
            ns = []
    for i, o in enumerate(op):
        if o:
            ans = 0
        else:
            ans = 1
        for r in opn[i]:
            if o:
                ans += r
            else:
                ans *= r
        part2 += ans
    return part2

#print(part1())
print(part2())
