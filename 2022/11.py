import sys

def op_add(v, fp):
    return v + fp

def op_mul(v, fp):
    return v * fp

def op_pow(v, fp):
    return v ** fp

def gen_func(str):
    seg = str.split()
    if seg[1] == '+':
        return op_add, int(seg[2])
    if seg[2] == 'old':
        return op_pow, 2
    return op_mul, int(seg[2])


lc = 0
m_id = 0
monkey_home = []
monkey_home2 = []
for line in sys.stdin:
    l = line.strip()
    if len(l) == 0:
        lc = 0
        continue

    if lc == 0:
        monkey_home.append({'start_item': [], 'inspect_count': 0})
        monkey_home2.append({'start_item': [], 'inspect_count': 0})
    elif lc == 1:
        monkey_home[-1]['start_item'] = [int(i) for i in l.split(': ')[1].split(', ')]
        monkey_home2[-1]['start_item'] = [int(i) for i in l.split(': ')[1].split(', ')]
    elif lc == 2:
        monkey_home[-1]['fun'], monkey_home[-1]['fun_param'] = gen_func(l.split('= ')[1])
        monkey_home2[-1]['fun'], monkey_home2[-1]['fun_param'] = gen_func(l.split('= ')[1])
    elif lc == 3:
        monkey_home[-1]['mod'] = int(l.split()[-1])
        monkey_home2[-1]['mod'] = int(l.split()[-1])
    elif lc == 4:
        monkey_home[-1]['y'] = int(l.split()[-1])
        monkey_home2[-1]['y'] = int(l.split()[-1])
    elif lc == 5:
        monkey_home[-1]['n'] = int(l.split()[-1])
        monkey_home2[-1]['n'] = int(l.split()[-1])
    lc += 1

def inspect(monkey_home, m3 = True, p = 1):
    for mk in monkey_home:
        while len(mk['start_item']) > 0:
            v = mk['start_item'].pop(0)
            nv = mk['fun'](v, mk['fun_param'])
            if m3:
                nv = nv // 3
            else:
                nv = nv % p
            if nv % mk['mod'] == 0:
                monkey_home[mk['y']]['start_item'].append(nv)
            else:
                monkey_home[mk['n']]['start_item'].append(nv)
            mk['inspect_count'] += 1

for i in range(20):
    inspect(monkey_home)

ic = [mk['inspect_count'] for mk in monkey_home]
m1 = max(ic)
ic.remove(m1)
m2 = max(ic)

print(m1*m2)

prod  = 1
for mk in monkey_home2:
    prod *= mk['mod']

for i in range(10000):
    inspect(monkey_home2, False, prod)

ic = [mk['inspect_count'] for mk in monkey_home2]
m1 = max(ic)
ic.remove(m1)
m2 = max(ic)

print(m1*m2)


