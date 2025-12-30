import sys
from functools import cmp_to_key

def get_sign(num):
    return (num > 0) - (num < 0)

def parse_line(line):
    stack = [[]]
    temp_l = []
    isint = False
    for c in line:
        if c == '[':
            temp_l = []
            stack.append(temp_l)
        elif c == ']':
            isint = False
            temp_l = stack.pop()
            stack[-1].append(temp_l)
        elif c.isdigit():
            if isint:
                stack[-1][-1] = stack[-1][-1] * 10 + int(c)
            else:
                isint = True
                temp_l = stack[-1]
                stack[-1].append(int(c))
        elif c == ',':
            isint = False
    return stack.pop()[0]

pairs = ([], [])
part2 = [[[2]], [[6]]]
for i, line in enumerate(sys.stdin):
    l = line.strip()
    if i % 3 == 2:
        continue
    pairs[i % 3].append(parse_line(l))
    part2.append(parse_line(l))


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return get_sign(right - left)
    if isinstance(left, list) and isinstance(right, list):
        ll = len(left)
        lr = len(right)
        for i in range(min(ll, lr)):
            res = compare(left[i], right[i])
            if res != 0:
                return res
        return get_sign(lr - ll)
    if isinstance(left, int):
        return compare([left], right)
    if isinstance(right, int):
        return compare(left, [right])

ans1 = 0
for i, left, right in zip(range(len(pairs[0])), pairs[0], pairs[1]):
    if compare(left, right) == 1:
        ans1 += i + 1

print(ans1)

part2.sort(reverse=True, key=cmp_to_key(compare))
print((part2.index([[2]]) + 1) * (part2.index([[6]]) + 1))
