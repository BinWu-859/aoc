import sys


fans1, fans2 = 0, 0
map = []
for line in sys.stdin:
    map.append(line.strip)

node_map = {
    '#':[],
    '.':[(-1, 0), (0, 1), (1, 0), (0, -1)],
    '>':[(0, 1)],
    '<':[(0, -1)],
    'v':[(1, 0)],
    '^':[(-1, 0)]
}

sc, sr = 0, map[0].index('.')

print(sr)


