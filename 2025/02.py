import sys
import math


def cal_invalid(a, b, digit):
    invalid = 0
    il = []
    if digit % 2 == 1 or digit < 2:
        return 0
    d = 1
    for i in range(digit//2):
        d *= 10
    d += 1

    for i in range(a, b + 1):
        if i % d == 0:
            invalid += i
    return invalid


def part1():
    for line in sys.stdin:
        ps = line.strip().split(',')
        invalid = 0
        for p in ps:

            l = p.split('-')
            start = int(l[0])
            sl = len(l[0])
            end = int(l[1])
            el = len(l[1])
            while True:
                if (sl == el):
                    invalid += cal_invalid(start, end, sl)
                    break
                invalid += cal_invalid(start, int('9' * sl), sl)
                sl += 1
                start = int('1' + '0' * (sl - 1))
    return invalid

def cal_invalid2(n):
    invalid = 0
    s = str(n)
    l = len(s)
    d = {}
    for i in range(1, len(s)//2 + 1):
        if l % i != 0:
            continue
        h = s[0:i]
        times = l // i
        if h * times == s:
            if n not in d:
                d[n] = True
                invalid += n
    return invalid

def part2():
    for line in sys.stdin:
        ps = line.strip().split(',')
        invalid = 0
        for p in ps:
            l = p.split('-')
            start = int(l[0])
            end = int(l[1])

            for n in range(start, end + 1):
                invalid += cal_invalid2(n)
    return invalid
print(part2())

