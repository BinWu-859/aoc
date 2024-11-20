import sys

def find_min(str):
    dict = {'green':0, 'blue':0, 'red':0, 'id':0}
    tmp = str.split(':')
    dict['id'] = int(tmp[0].split()[1])
    turns = tmp[1].split(';')

    for i in turns:
        items = i.split(',')
        for j in items:
            d = j.split()
            dict[d[1]] = max(dict[d[1]], int(d[0]))
    return dict

def ans01(dict, bar):
    if bar['green'] < dict['green'] or bar['blue'] < dict['blue'] or bar['red'] < dict['red']:
        return 0
    return dict['id']

def ans02(dict):
    return dict['blue'] * dict['red'] * dict['green']

fans1 = 0
fans2 = 0
for line in sys.stdin:
    if '' == line.rstrip():
        break
    dict = find_min(line)
    fans1 = fans1 + ans01(dict ,{'green':13, 'blue':14, 'red':12})
    fans2 = fans2 + ans02(dict)
print(fans1, fans2)

