import sys

line = sys.stdin.readline()
# speed up with set
patterns = set(line.strip().split(', '))

pmax = max([len(i) for i in patterns])

def run(s):
    pmap = {}
    nmap = {}
    stk = [(s, [])]
    while stk:
        cs, hist = stk.pop()
        if cs == ''  or (cs in pmap):
            c = 1
            if cs in pmap:
                c = pmap[cs]

            for i in hist:
                if i in pmap:
                    pmap[i] += c
                else:
                    pmap[i] = c
            continue

        if cs in nmap:
            # skip cached negative cases
            # although some positive cases are also included in the nmap, but
            # never mind, b'z pmap is prioritized
            continue
        nmap[cs] = 0
        hist.append(cs)
        for i in range(min(len(cs), pmax)):
            if cs[:i+1] in patterns:
                #print(cs,cs[:i+1], '->', cs[i+1:], hist)
                stk.append((cs[i+1:], hist.copy()))

    return pmap[s] if s in pmap else 0

line = sys.stdin.readline()
fans1 = 0
fans2 = 0
for line in sys.stdin:
    n = run(line.strip())
    if n > 0:
        fans1 += 1
        fans2 += n
    #print(n, line)

print(fans1, fans2)
