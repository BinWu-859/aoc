import sys

def mapv(p, seed):
    for i in p:
        if seed >= i[1] and seed <= i[1] + i[2] - 1:
            return seed - i[1] + i[0]
    return seed


def ans01(paths, seed):
    tmp = seed
    for p in paths:
        tmp = mapv(p, tmp)
    return tmp

def calc_range(paths, depth, s, e):
    ans=[ ]
    #print(' -> dep {}/{}, s {}, e {}'.format(depth, len(paths), s, e))
    if depth == len(paths):
        #print(' <- dep {}, ({}, {}) = {}'.format(depth, s, e, s))
        return s

    for p in paths[depth]:
        ins, ine = calc_intersection(s, e, p[1], p[1] + p[2])
        if ins >= ine:
            # No intersection
            continue
        #print('in', ins, ine)
        if ins > s:
            # Have left splitted range
            ans.append(calc_range(paths, depth, s, ins))

        if ine < e:
            # Hav right splitted range
            ans.append(calc_range(paths, depth, ine, e))
        ans.append(calc_range(paths, depth + 1, ins - p[1] + p[0], ine - p[1] + p[0]))
        #print('p {}, ({}, {}) '.format(p, ins, ine), ans)
        break
    if len(ans) == 0:
        ans.append(calc_range(paths, depth + 1, s, e))
    #print(' <- dep {}, ({}, {}) = {}'.format(depth, s, e, ans))
    return min(ans)




def calc_intersection(s1, e1, s2, e2):
    if e1 == -1:
        return (max(s1, s2), e2)
    if e2 == -1:
        return (max(s1, s2), e1)
    return (max(s1, s2), min(e1, e2))

def com_range(e):
    return e[1]

fans1 = 0
fans2 = 0
paths = []
# y, x, range

path_queue = []
for line in sys.stdin:
    seeds = [int(i) for i in line.split(':')[1].split()]
    break

path = []
for line in sys.stdin:
    if 'map:' in line:
        path = []
        continue
    if "\n" == line and len(path) > 0:
        paths.append(path)
        continue
    path.append([int(i) for i in line.split()])
paths.append(path)

tans = [ans01(paths, i) for i in seeds]
print(tans)
fans1 = min(tans)



ans02 = []
for i in range(0, len(seeds)//2, 1):
    s = seeds[2*i]
    r = seeds[2*i+1]
    #print('\n=====', s, s+r)

    ans02.append(calc_range(paths, 0, s, s + r))


print(fans1, min(ans02))

