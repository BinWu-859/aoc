import sys
import re

fans1, fans2 = 0, 0
go = True
for line in sys.stdin:
    ret = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
    for l in ret:
        if l == r"do()":
            go = True
            continue
        if l == r"don't()":
            go = False
            continue
        a = re.findall(r"\d{1,3}", l)
        fans1 += int(a[0]) * int(a[1])
        if go:
            fans2 += int(a[0]) * int(a[1])

print(fans1, fans2)

