import sys



def strip_head(code, count):
    if len(code) == 0 or len(code[0]) == 0 or len(count) == 0:
        return False
    if code[0].find('#') != -1:
        if len(code[0]) < count[0]:
            return False
    if len(code[0]) == count[0]:
        code.pop(0)
        count.pop(0)
    while code and code[0][0] == '#':
        code[0] = code[0][1:]
        count[0] -= 1
        if count[0]==0:
            count.pop(0)
            if len(code[0]) > 0:
                if code[0][0] == '#':
                    return False
                else:
                    code[0] = code[0][1:] #eat '?'
        if code[0] == '':
            code.pop(0)
    return True
def calc(code, count):
    print('calc ', code, count)
    if not strip_head(code, count):
        print(" -> 0")
        return 0
    if len(code) == 0:
        print(" -> 1")
        return 1
    gcode1 = code.copy()
    gcode2 = code.copy()
    # ? -> .
    gcode1[0] = code[0][1:]
    # ? -> #
    gcode2[0] = '#'+code[0][1:]
    print('next ', gcode1, gcode2, count)
    return calc(gcode1, count.copy()) + calc(gcode2, count.copy())

def ans01(code, count):
    ans = 1
    rc = [i for i in filter(lambda x: x, code.split('.'))]
    ans = calc(rc, count)
    return ans

fans1 = 0
fans2 = 0

for line in sys.stdin:
    line = line.strip().split()
    fans1 += ans01(line[0], [int(i) for i in line[1].split(',')])


print(fans1, fans2)

