import sys

def get_card_value(c):
    vmap = {'A': 14,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            }
    if c not in vmap:
        return 0
    return vmap[c]
def get_card_value2(c):
    vmap = {'A': 14,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 1,
            'Q': 12,
            'K': 13,
            }
    if c not in vmap:
        return 0
    return vmap[c]


def get_rank(h):

    h.sort(key = get_card_value)
    if h[0] == h[1] and h[1] == h[2] and h[2] == h[3] and h[3] == h[4]:
        return 7
    if (h[0] == h[1] and h[1] == h[2] and h[2] == h[3]) or ( h[1] == h[2] and h[2] == h[3] and h[3] == h[4]):
        return 6
    if (h[0] == h[1] and h[1] == h[2] and h[3] == h[4]) or ( h[0] == h[1] and h[2] == h[3] and h[3] == h[4]):
        return 5
    if (h[0] == h[1] and h[1] == h[2]) or (h[2] == h[3] and h[3] == h[4]) or (h[1] == h[2] and h[2] == h[3]):
        return 4
    d = 0
    for i in range(1, 5, 1):
        if h[i] == h[i-1]:
            d += 1
    if d == 2:
        return 3
    if d == 1:
        return 2
    return 1


def get_most_card(h):
    c = {}
    for i in h:
        if i not in c:
            c[i] = 1
        else:
            c[i] += 1
    l = list(c.items())
    l.sort(key=lambda a : a[1], reverse = True)
    return l[0][0]

def get_rank2(h):
    h.sort(key = get_card_value2)
    #print(h)
    jc = 0
    for i in h:
        if i == 'J':
            jc += 1
    if jc == 0:
        return get_rank(h)
    if jc == 5 or jc == 4:
        return 7

    nj = get_most_card(h[jc:])

    for i, c in enumerate(h):
        if c == 'J':
            h[i] = nj
    #print('->',h)
    return get_rank(h)


def get_sub_score(e):
    s = 0
    for i in e:
        s = s*16 + get_card_value(i)
    return s;
def get_sub_score2(e):
    s = 0
    for i in e:
        s = s*16 + get_card_value2(i)
    return s;

def ans01(e):
    sub_score = get_sub_score(e[0])
    return get_rank(list(e[0])) * 16**5 + sub_score

def ans02(e):
    sub_score = get_sub_score2(e[0])
    return get_rank2(list(e[0])) * 16**5 + sub_score

fans1 = 0
fans2 = 0


hands = []

for line in sys.stdin:
    hands.append(tuple(line.split()))


hands.sort(key=ans01)
#print(hands)

for i, h in enumerate(hands):
    fans1 += (i + 1) * int(h[1])

hands.sort(key=ans02)
#print(hands)

for i, h in enumerate(hands):
    fans2 += (i + 1) * int(h[1])

print(fans1, fans2)

