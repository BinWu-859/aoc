import sys


turns = []
fans1 = 0
fans2 = 0
# R P S
map = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}


def score(c):
    if map[c[0]] == map[c[1]]:
        return map[c[1]]+3
    if map[c[1]] == 1:
        return map[c[1]]+6 if map[c[0]] == 3 else map[c[1]]
    if map[c[1]] == 2:
        return map[c[1]]+6 if map[c[0]] == 1 else map[c[1]]
    if map[c[1]] == 3:
        return map[c[1]]+6 if map[c[0]] == 2 else map[c[1]]


def score2(c):
    if c[1] == 'Y':
        return map[c[0]]+3
    if map[c[0]] == 1:
        return 3 if c[1] == 'X' else 2+6
    if map[c[0]] == 2:
        return 1 if c[1] == 'X' else 3+6
    if map[c[0]] == 3:
        return 2 if c[1] == 'X' else 1+6

for line in sys.stdin:
    l = line.strip().split()
    fans1 += score(l)
    fans2 += score2(l)

print(fans1, fans2)
