import sys

def find_max(str):
    max = '0'
    maxi = -1
    for i, v in enumerate(str):
        if v > max:
            max = v
            maxi = i
    return int(max), maxi

def find_batteries(l, s):
    ci = -1
    ta = 0
    for i in range(s):
        slice = -(s - i - 1)
        if slice >= 0:
            slice = len(l)
        a, ai = find_max(l[ci + 1 :slice])
        ci += (ai + 1)
        ta = 10 * ta + a
    return ta

def part1(lines):
    ans = 0
    for l in lines:
        ans += find_batteries(l, 2)
    return ans

def part2(lines):
    ans = 0
    for l in lines:
        ans += find_batteries(l, 12)
    return ans

lines=[]
for line in sys.stdin:
    lines.append(line.strip())

print(part1(lines), part2(lines))

