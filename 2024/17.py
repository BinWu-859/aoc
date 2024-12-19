import sys

REG = {}
for i in sys.stdin:
    if len(i.strip()) == 0:
        break
    l = i.strip().split()
    REG[l[1][0]]=int(l[2])
print(REG)

prog = sys.stdin.readline().strip().split()[1].split(',')
print(prog)

def get_cb_v(cb):
    if cb in '0123':
        return int(cb)
    if cb == '4':
        return REG['A']
    if cb == '5':
        return REG['B']
    if cb == '6':
        return REG['C']
def run():
    out = []
    i = 0
    while i < len(prog) - 1:
        op = prog[i]
        cb = prog[i + 1]
        i += 2

        if op == '0':
            REG['A'] = REG['A']//2**get_cb_v(cb)
            continue
        if op == '1':
            REG['B'] = REG['B'] ^ int(cb)
            continue
        if op == '2':
            REG['B'] = get_cb_v(cb)%8
            continue
        if op == '3':
            if REG['A'] != 0:
                i = int(cb)
            continue
        if op == '4':
            REG['B'] = REG['B'] ^ REG['C']
            continue
        if op == '5':
            out.append('{}'.format(get_cb_v(cb)%8))
            continue
        if op == '6':
            REG['B'] = REG['A']//2**get_cb_v(cb)
            continue
        if op == '7':
            REG['C'] = REG['A']//2**get_cb_v(cb)
            continue
    return out
#part1
print(','.join(run()))
#part2
# 2,4 -> B = A%8
# 1,1 -> flip last bit
# 7,5 -> C = A//2**5
# 0,3,-> A = A//2**3
# 1,4 -> flip 2rd last bit
# 4,4,-> XOR B&C
# 5,5,-> print out first
# 3,0 loop log(8, A) times

# first digit 1024 loops
# second digit  and later repeat 8 times in each digits
d=[[] for i in range(4)]
ans2 = 0
for i in range(1024):
    REG['A'] = i
    REG['B'] = 0
    REG['C'] = 0
    r = run()
    #d.append(r[0])
    for j,l in enumerate(r):
        d[j].append(l)


#find full set of program
#print(d[0])
fans2 = 0
offset=[0]*len(prog)

def go_down(cur, mx):
    down = True
    while True:
        p = d[0][offset[cur] % 1024:].index(prog[cur])
        #print('F',prog[cur] , offset[cur]%1024, p )
        offset[cur] += p
        if offset[cur - 1] < 8 * offset[cur]:
            offset[cur - 1] = 8 *offset[cur]
            np = d[0][offset[cur - 1] % 1024:].index(prog[cur - 1])
            #print('F',prog[cur - 1] , offset[cur - 1]%1024, np )
            offset[cur - 1] += np
            #print('S', cur - 1, offset[cur - 1])
        if offset[cur - 1] >= (offset[cur] + 1) * 8:
            offset[cur] = offset[cur - 1] //8
            #print('S', cur, offset[cur - 1]//8)
            down = False
        else:
            break
    return down

def go_up(cur, mx):
    down = False
    if cur == mx - 1:
        return True
    while True:
        p = d[0][offset[cur] % 1024:].index(prog[cur])
        #print('F',prog[cur] , offset[cur]%1024, p )
        offset[cur] += p
        if offset[cur] >= (offset[cur + 1] + 1) * 8:
            offset[cur + 1] = (offset[cur])//8
            np = d[0][offset[cur + 1] % 1024:].index(prog[cur + 1])
            offset[cur + 1] += np
            #print('S', cur + 1, offset[cur + 1])
            offset[cur] = 8 * offset[cur + 1]
            #print('S', cur, offset[cur])
        else:
            down = False
            break
    return down
mx = 16
cur = mx-1
down=True
while True:

    if down:
        if cur == 0:
            if offset[0] < 8**(mx - 1):
                down = False
                cur = 0
                offset[0] = 8**(mx - 1)
                continue
            break
        down = go_down(cur, mx)
        if down:
            cur -= 1

    else:
        down = go_up(cur, mx)
        if not down:
            cur += 1
    #print(cur)
print(offset[0])








