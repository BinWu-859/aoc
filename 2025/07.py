import sys

def solve():
    ans1 = 0
    ans2 = 0
    map = []
    length = 0
    for i, line in  enumerate(sys.stdin):
        marks = {}
        if i%2 == 1:
            continue
        l = line.strip()
        if i == 0:
            length = len(l)
            marks[l.find('S')] = None
        else:
            for j, c in  enumerate(l):
                if c == '^':
                    marks[j] = None
        map.append(list(marks.keys()))
    #print(map)

    stack = [{map[0][0]:1}]
    for l in map[1:]:
        m = stack.pop()
        n = {}
        for k in m:
            if k in l:
                if k-1 not in n :
                    n[k-1] = m[k]
                else:
                    n[k-1] += m[k]
                if k+1 not in n :
                    n[k+1] = m[k]
                else:
                    n[k+1] += m[k]
                ans1 += 1
            else:
                if k not in n:
                    n[k] = m[k]
                else:
                    n[k] += m[k]
        stack.append(n)
    for i in stack[0].values():
        ans2 += i

    return ans1, ans2

print(solve())
