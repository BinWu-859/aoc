import sys

ct = []
cc = 0
for line in sys.stdin:
    l = line.strip()
    if len(l) == 0:
        ct.append(cc)
        cc = 0
        continue
    cc += int(l)
ct.append(cc)

ans2 = 0
ct2 = ct.copy()
for i in range(3):
    m = max(ct2)
    ans2 += m
    ct2.remove(m)
print(max(ct), ans2)
