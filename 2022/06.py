import sys

l = sys.stdin.readline().strip()

def p(n):
    for i in range(n, len(l) + 1):
        win = l[i-n:i]
        if len(set(list(win))) == n:
            return i
    return None

print(p(4), p(14))