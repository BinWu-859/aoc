import sys

num = 100
pos = 50
ans = 0

def part1(num, pos, ans):
    for line in sys.stdin:
        l = line.strip()
        step = int(l[1:])

        step = step % num

        if l[0] == 'L':
            pos -= step

        else:
            pos += step


        pos = pos % num
        if pos == 0:
            ans += 1
    return ans

def part2(num, pos, ans):
    for line in sys.stdin:
        l = line.strip()
        step = int(l[1:])

        ans += step // num # for part 2
        step = step % num

        if l[0] == 'L':
            pos -= step
            if pos < 0 and pos + step != 0:
                ans += 1
        else:
            pos += step
            if pos > num:
                ans += 1

        pos = pos % num
        if pos == 0:
            ans += 1
    return ans

print(part2(num, pos, ans))

