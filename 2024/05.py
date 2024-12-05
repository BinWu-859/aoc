import sys

rel = {}

def correct_order(cmap, rel, f, s):
    return cmap[f].count(s) > 0
    # Patterns like A|B B|C C|A will all present in the input data
    # It does not make sense to calculate the indirect order
    # if (f, s) in rel:
    #     return rel[(f,s)]
    # stk =[cmap[f]]
    # print('push', f, cmap[f])
    # while stk:
    #     l = stk.pop()
    #     if l.count(s) > 0:
    #         rel[(f,s)] = True
    #         return True
    #     for i in l:
    #         if len(cmap[i]) > 0:
    #             print('push', i, cmap[i])
    #             stk.append(cmap[i])
    # rel[(f,s)] = False
    # return False

def correct_p(cmap, rel, ps):
    for i in range(len(ps) - 1):
        for j in range(1, len(ps) - i):
            if not correct_order(cmap, rel, ps[j - 1], ps[j]):
                tmp = ps[j]
                ps[j] = ps[j - 1]
                ps[j - 1] = tmp
    return ps

fans1, fans2 = 0, 0
cmap = {}

for line in sys.stdin:
    l = line.strip().split('|')
    if len(l) < 2:
        break
    if l[0] not in cmap:
        cmap[l[0]] = [l[1]]
    else:
        cmap[l[0]].append(l[1])
    if l[1] not in cmap:
        cmap[l[1]] = []


for line in sys.stdin:
    ps = line.strip().split(',')
    correct = True
    for i, p in enumerate(ps):
        if i == 0:
            continue
        if not correct_order(cmap, rel, ps[i-1], p):
            correct = False
            break
    if correct:
        fans1 += int(ps[len(ps)//2])
    else:
        cps = correct_p(cmap, rel, ps)
        fans2 += int(cps[len(cps)//2])

print(fans1, fans2)

