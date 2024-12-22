import sys



def sign(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0

dir_map = {
    (1, 0):'v',
    (-1, 0):'^',
    (0, 1): '>',
    (0, -1): '<',
    (0, 0): 'A'
}
dir_map_r = {
    'v':(1, 0),
    '^':(-1, 0),
    '>':(0, 1) ,
    '<':(0, -1)
}
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A*|
#     +---+---+
num_key = {
        '0': (3, 1),
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2),
        'A': (3, 2)
    }
num_pos = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['!', '0', 'A']
]
#     +---+---+
#     | ^ | A*|
# +---+---+---+
# | < | v | > |
# +---+---+---+
dir_key = {
        '^': (0, 1),
        '<': (1, 0),
        'v': (1, 1),
        '>': (1, 2),
        'A': (0, 2)
    }
dir_pos = [
    ['!', '^', 'A'],
    ['<', 'v', '>']
]



def pad(key, pos, l):
    s = 'A'
    fret = []
    for gp in l:
        ops = []
        for ins in gp:
            op = []
            mr = key[ins][0] - key[s][0]
            mc = key[ins][1] - key[s][1]
            v = dir_map[(0, sign(mc))] * abs(mc)
            h = dir_map[(sign(mr), 0)] * abs(mr)
            if mr == 0:
                op.append(v +'A')
            elif mc == 0:
                op.append(h +'A')
            else:
                c1 = ''.join([v, h]) + 'A'
                c2 = ''.join([h, v]) + 'A'

                if pos[key[s][0]][key[ins][1]] != '!':
                    op.append(c1)
                if pos[key[ins][0]][key[s][1]] != '!':
                    op.append(c2)
            s = ins
            ops.append(op)
        #print('ops', ops)
        ret = ['']
        for op in ops:
            nret = []
            for i in op:
                for j in ret:
                    nret.append(''.join([j, i]))
            ret = nret
        for i in ret:
            fret.append(i)
    return fret


# Way to verify, not part of solution
def press(key, pos, l):
    ret = []
    s = key['A']
    nr = s[0]
    nc = s[1]
    for i in l:
        if i == 'A':
            ret.append(pos[nr][nc])
            continue
        d = dir_map_r[i]
        nr += d[0]
        nc += d[1]
        if pos[nr][nc] == '!':
            print('Segment Fault!')
    return ret

if False:
    i = 'v<<A>>^AAAvA^Av<<A>A>^A<A>vA^Av<A<AA>>^AvAA^<A>A<vA<A>>^AAvA^A<A>A'

    k1 = press(dir_key, dir_pos, i)
    print(k1)
    k1 = press(dir_key, dir_pos, k1)
    print(k1)
    k1 = press(num_key, num_pos, k1)
    print(k1)


v2 = {}
vk = []
for i in range (len(num_pos)):
    for j in range (len(num_pos[0])):
        for v in 'v^':
            for h in '<>':
                vk.append(v*i + h*j +'A')
                vk.append(h*j + v*i +'A')
vk = list(set(vk))

for i in vk:
    op = [i]
    for j in range(2):
        tp = pad(dir_key, dir_pos, op)
        a = min([len(i) for i in tp])
        op = tp
    v2[i] = a

#{'A': 1, 'vA': 16, '^A': 12, 'vvA': 17, '^^A': 13, '<A': 18, '>A': 10,
# 'v<A': 25, '<vA': 21, 'v>A': 17, '>vA': 21, '^<A': 25, '<^A': 21, '^>A': 19,
# '>^A': 19, 'vv<A': 26, '<vvA': 22, 'vv>A': 18, '>vvA': 22, '^^<A': 26,
# '<^^A': 22, '^^>A': 20, '>^^A': 20, '<<A': 19, '>>A': 11, 'v<<A': 26,
# '<<vA': 22, 'v>>A': 18, '>>vA': 22, '^<<A': 26, '<<^A': 22, '^>>A': 20,
# '>>^A': 20, 'vv<<A': 27, '<<vvA': 23, 'vv>>A': 19, '>>vvA': 23, '^^<<A': 27,
# '<<^^A': 23, '^^>>A': 21, '>>^^A': 21, '<<<A': 20, '>>>A': 12, 'v<<<A': 27,
# '<<<vA': 23, 'v>>>A': 19, '>>>vA': 23, '^<<<A': 27, '<<<^A': 23, '^>>>A': 21,
# '>>>^A': 21, 'vv<<<A': 28, '<<<vvA': 24, 'vv>>>A': 20, '>>>vvA': 24, '^^<<<A': 28, '<<<^^A': 24, '^^>>>A': 22, '>>>^^A': 22}
# so '<^A' better than '^<A'
#    '>^A' better than '^>A'
#    '<vA' better than 'v<A'
#    'v>A' better than '>vA'
def get_score(p, v):
    if p not in v:
        return 1000
    return v[p]

def pad2(key, pos, l):
    '''
    Use v2 to choose a better choice
    '''
    s = 'A'
    fret = []
    for gp in l:
        ops = []
        for ins in gp:
            op = ''
            mr = key[ins][0] - key[s][0]
            mc = key[ins][1] - key[s][1]
            v = dir_map[(0, sign(mc))] * abs(mc)
            h = dir_map[(sign(mr), 0)] * abs(mr)
            if mr == 0:
                op=(v +'A')
            elif mc == 0:
                op=(h +'A')
            else:
                c1 = ''.join([v, h]) + 'A'
                c2 = ''.join([h, v]) + 'A'
                m1 = get_score(c1, v2)
                m2 = get_score(c2, v2)
                if m1 < m2:
                    if pos[key[s][0]][key[ins][1]] != '!':
                        op = c1
                    else:
                        op = c2
                else:
                    if pos[key[ins][0]][key[s][1]] != '!':
                        op = c2
                    else:
                        op = c1

            s = ins
            ops.append(op)
        fret.extend(ops)
    return fret

codes = []
for line in sys.stdin:
    codes.append(line.strip())


def run(n):
    ans = 0
    for l in codes:
        b = int(l[:-1])
        op = pad2(num_key, num_pos, [l])
        for i in range(n):
            op = pad2(dir_key, dir_pos, op)
        a = sum([len(i) for i in op])
        ans += a * b
    return ans


#build cache key

ck = []
for i in range (len(dir_pos)):
    for j in range (len(dir_pos[0])):
        for v in 'v^':
            for h in '<>':
                ck.append(v*i + h*j +'A')
                ck.append(h*j + v*i +'A')
ck = list(set(ck))

def run25():
    cache = {}
    ans = 0
    # build a 12-turn cache, will reduce total calculation turns from 25 to 13
    for l in ck:
        op = [l]
        for i in range(12):
            op = pad2(dir_key, dir_pos, op)
        ta = sum([len(i) for i in op])
        cache[l] = (ta, op)

    for l in codes:
        a = 0
        b = int(l[:-1])
        op = pad2(num_key, num_pos, [l])
        op = pad2(dir_key, dir_pos, op)
        nop = []
        for i in op:
            nop.extend(cache[i][1])
        for i in nop:
            # no need to construct instructions
            a += cache[i][0]

        #print(a, b)
        ans += a * b
    return ans

print(run(2), run25())

