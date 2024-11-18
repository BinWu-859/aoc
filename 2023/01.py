import sys

def convert(str, r):
    if not r:
        str = str.replace('twone', '2ne')
        str = str.replace('eightwo', '8wo')
        str = str.replace('eighthree', '8hree')
        str = str.replace('one', '1')
        str = str.replace('two', '2')
        str = str.replace('three', '3')
        str = str.replace('four', '4')
        str = str.replace('five', '5')
        str = str.replace('six', '6')
        str = str.replace('seven', '7')
        str = str.replace('eight', '8')
        str = str.replace('nine', '9')
    else:
        str = str.replace('oneight', 'on8')
        str = str.replace('threeight', 'thre8')
        str = str.replace('fiveight', 'fiv8')
        str = str.replace('sevenine', 'seve9')
        str = str.replace('one', '1')
        str = str.replace('two', '2')
        str = str.replace('three', '3')
        str = str.replace('four', '4')
        str = str.replace('five', '5')
        str = str.replace('six', '6')
        str = str.replace('seven', '7')
        str = str.replace('eight', '8')
        str = str.replace('nine', '9')
    return str

def ans02(str):
  return ans01(convert(str, False), convert(str, True))

def ans01(str, bstr = ""):
    ans = 0
    if not bstr:
        rstr = reversed(str)
    else:
        rstr = reversed(bstr)
    for c in str:
        if c.isdigit():
            ans = int(c) * 10
            break
    for c in rstr:
        if c.isdigit():
            ans = ans + int(c)
            break
    return ans

fans1 = 0
fans2 = 0
for line in sys.stdin:
    if '' == line.rstrip():
        break
    tans1 = ans01(line)
    tans2 = ans02(line)
    #print(line, tans1, tans2)
    fans1 = fans1 + tans1
    fans2 = fans2 + tans2
print(fans1, fans2)

