import sys
import math

def get_value(c):
    cc = ord(c)
    ca = ord('a')
    if cc >= ca:
        return ord(c) - ord('a')
    else:
        return ord(c) - ord('A') + 26

fans1 = 0
fans2 = 0
part2 = []
for i, l in enumerate(sys.stdin):
    line = l.strip()
    s = len(line)
    left = 0
    right = 0
    full = 0
    for c in line[:s//2]:
        left = (left | (1 << get_value(c)))
        full = full | left
    for c in line[s//2:]:
        right = (right | (1 << get_value(c)))
        full = full | right
    com = left & right
    fans1 += (int(math.log2(com)) + 1)
    part2.append(full)
    if i % 3 == 2:
        com2 = part2[0] & part2[1] & part2[2]
        fans2 += (int(math.log2(com2)) + 1)
        part2 = []
print(fans1, fans2)




