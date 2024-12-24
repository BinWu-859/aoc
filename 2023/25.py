import sys
import networkx as nx
from networkx.algorithms.connectivity import minimum_st_edge_cut
map = {}

G = nx.Graph()

s = None
for line in sys.stdin:
    c = line.strip().split(': ')
    l = c[0]
    if not s:
        s = l
    r = c[1].split()
    for i in r:
        if l not in map:
            map[l] = {}
        map[l][i] = 0
        G.add_edge(l, i)
        if i not in map:
            map[i] = {}
        map[i][l] = 0
        G.add_edge(i, l)

for i in map:
    if i == s:
        continue
    mc = minimum_st_edge_cut(G, s, i)
    if len(mc) == 3:
        print(mc)
        for e in mc:
            G.remove_edge(e[0], e[1])
        break
sn = len(list(nx.node_connected_component(G, s)))
print(sn * (len(map) - sn))