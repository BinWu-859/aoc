import sys

cache = {}
def strip_head(code, num):
    # '' 0
    # '#' 0
    # '?' 0
    # '?' 1
    # '' 1
    fnum = sum(num)
    snum = sum([i.count('#') for i in code])
    # print(code, num, snum, fnum)
    if snum > fnum:
        return False
    if snum == 0 and fnum == 0:
        return True
    if not code and fnum > 0:
        return False
    # Fast forward
    if fnum > sum([len(i) for i in code]):
        return False

    # Fast forward
    if not code[0] and fnum > 0:
        code.pop(0)
        return strip_head(code, num)

    if code[0].find('#') != -1:
        if len(code[0]) < num[0]:
            return False
        # Fast forward
        if len(code[0]) == num[0]:
            code.pop(0)
            num.pop(0)
            return strip_head(code, num)
    if code[0].find('#') == -1 and len(code[0]) < num[0]:
        code.pop(0)
        return strip_head(code, num)
    if code[0][0] == '#':
        code[0] = code[0][num[0]:]
        num.pop(0)
        if len(code[0]) > 0:
            if code[0][0] == '#':
                return False
            else:
                code[0] = code[0][1:] #eat '?'
        else:
            code.pop(0)
        return strip_head(code, num)
    return True
def to_key(code, num):
    k = '|'.join(code)
    for i in num:
        k = k + '{}|'.format(i)
    return k
def calc(code, num, l):
    global cache
    if not strip_head(code, num):
        # print(l*'-', " -> 0")
        return 0
    if sum([i.count('#') for i in code]) == 0 and sum(num) == 0:
        # print(l*'-', " -> 1")
        return 1
    k = to_key(code, num)
    if k in cache:
        #print('HIT!', k)
        return cache[k]
    gcode1 = code.copy()
    gcode2 = code.copy()
    # ? -> .
    gcode1[0] = code[0][1:]
    # ? -> #
    gcode2[0] = '#'+code[0][1:]

    ret1 = calc(gcode1, num.copy(), l+1)
    ret2 = calc(gcode2, num.copy(), l+1)
    #print(l*'-', '==>',code,num, ret1, ret2, ret1+ret2)
    cache[k] = ret1 + ret2
    return ret1+ret2
def ans01(code, count):

    rc = [i for i in filter(lambda x: x, code.split('.'))]
    ans = calc(rc, count, 0)
    print('==>',code,count, ans)
    return ans
def ans02(code, count):
    code = '?'.join([code] * 5)
    count = count * 5
    rc = [i for i in filter(lambda x: x, code.split('.'))]
    ans = calc(rc, count, 0)
    print('==>',code,count, ans)
    return ans
fans1 = 0
fans2 = 0

for line in sys.stdin:
    line = line.strip().split()
    fans1 += ans01(line[0], [int(i) for i in line[1].split(',')])
    fans2 += ans02(line[0], [int(i) for i in line[1].split(',')])


print(fans1, fans2)

