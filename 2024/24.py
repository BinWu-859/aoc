import sys

map = {}

ovmap = {}
for line in sys.stdin:
    if len(line.strip()) == 0:
        break
    l = line.strip().split(': ')
    ovmap[l[0]] = int(l[1])
op = {}
op_o = {}
op_r = {}
for line in sys.stdin:
    l = line.strip().split(' -> ')
    op[l[1]] = l[0].split()
    op_o[l[1]] = l[0]
    op_r[l[0]] = l[1]
def run(ops):
    vmap = ovmap.copy()
    while len(ops) > 0:
        stk = [list(ops.keys())[0]]
        while stk:
            r = stk.pop()
            if ops[r][0] in vmap and ops[r][2] in vmap:
                if ops[r][1][0] == 'O':
                    vmap[r] = vmap[ops[r][0]] | vmap[ops[r][2]]
                if ops[r][1][0] == 'A':
                    vmap[r] = vmap[ops[r][0]] & vmap[ops[r][2]]
                if ops[r][1][0] == 'X':
                    vmap[r] = vmap[ops[r][0]] ^ vmap[ops[r][2]]

                ops.pop(r)
                continue
            if ops[r][0] not in vmap:
                stk.append(ops[r][0])
            if ops[r][2] not in vmap:
                stk.append(ops[r][2])
    return vmap

def compute(v, c):
    ret = 0
    for i in v:
        if i[0] == c and v[i] == 1:
            ret += (1 << int(i[1:]))
    return ret
res1 = run(op.copy())
ans1 = compute(res1, 'z')
print(ans1)


bits = len(ovmap)//2

def get_res(n1, l, n2, a):
    d = {'A':'AND', 'O':'OR', 'X':'XOR'}
    k1 = ' '.join([n1, d[l], n2])
    k2 = ' '.join([n2, d[l], n1])
    if k1 in op_r:
        return op_r[k1]
    if k2 in op_r:
        return op_r[k2]
    print('get_res ', a, n1, l , n2)
    return None
part2 = []
# Part2
# Half auto solution :D
# Z0 = X0 XOR Y0;  C0 = X0 AND Y0
# Z1 = B1 XOR C0;  B1 = (X01 XOR Y01); E1 = B1 AND C0; D1 = X01 AND Y01; C1 = E1 OR D1
# Zn = Bn XOR Cn-1; Bn = (Xn XOR Yn); Dn = Xn AND Yn; En = (Bn AND Cn-1) Cn = En OR Dn
#Z0
def swap(f1, f2):
    part2.append(f1)
    part2.append(f2)
    t = op_r[op_o[f1]]
    op_r[op_o[f1]] = op_r[op_o[f2]]
    op_r[op_o[f2]] = t
    print (op_o[f2], '->',t)
    print (op_o[f1], '->',op_r[op_o[f1]])
def run2():
    B = []
    C = []
    D = []
    E = []
    key = 'z01'
    if op[op[key][0]][1][0] == 'A':
        B.append('   ') #B0
        B.append(op[key][0]) #B1
        C.append(op[key][2]) #C0
    else:
        B.append('   ') #B0
        B.append(op[key][2]) #B1
        C.append(op[key][0]) #C0
    D.append('   ')
    E.append('   ')
    #Z1
    D.append(get_res('x01', 'A', 'y01', 'd1'))
    E.append(get_res(B[1], 'A', C[0], 'e1'))
    C.append(get_res(D[1], 'O', E[1], 'c1'))

    for i in range(2, bits):
        n_str = '{:02d}'.format(i)
        # Should always work
        b = get_res('x'+n_str, 'X', 'y'+n_str, f'b{i}')
        f1 = 'z'+ n_str
        f2 = get_res(b, 'X', C[i-1], f'z{i}')
        if not f2:
            k = op_o[f1].split()
            ff = []
            for j in [b, C[i - 1]]:
                if j not in [k[0], k[2]]:
                    ff.append(j)
            for j in [k[0], k[2]]:
                if j not in [b, C[i - 1]]:
                    ff.append(j)
            swap(ff[0], ff[1])
            return False
        if f1 != f2:
            print(b, 'X', C[i-1], 'should be', f1, 'but', f2)
            swap(f1, f2)
            return False
        # Should always work
        d = get_res('x{:02d}'.format(i), 'A', 'y{:02d}'.format(i), f'd{i}')
        # Should always work because get_res(b, 'X', C[i-1], f'z{i}') is OK
        e = get_res(b, 'A', C[i - 1], f'e{i}')
        c = get_res(e, 'O', d, f'c{i}')
        if not c:
            ff = [e]
            for lt in op_r.keys():
                o = lt.split()
                if o[1][0] != 'O':
                    continue
                if o[0] == d:
                    ff.append(o[2])
                if o[1] == d:
                    ff.append(o[0])
                swap(ff[0], ff[1])
                return False

        B.append(b)
        C.append(c)
        D.append(d)
        E.append(e)
    return True
while not run2():
    pass
part2.sort()
print(','.join(part2))

