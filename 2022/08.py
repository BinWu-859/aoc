import sys
import numpy as np

map=[]
for line in sys.stdin:
    map.append([int(i) for i in line.strip()])
npmap = np.array(map)

fans1 = 2 * len(map) + 2 *len(map[0]) - 4
scores = []
for i in range(1, len(map) - 1):
    for j in range(1, len(map[0]) - 1):
        visible = False
        score = 1
        for l in [npmap[i-1::-1, j], npmap[i+1:, j], npmap[i, j-1::-1], npmap[i, j+1:]]:
            if max(l) < npmap[i, j]:
                visible = True
            ts = len(l)
            for c,k in enumerate(l):
                if k >= npmap[i, j]:
                    ts = c+1
                    break
            score *= ts
        scores.append(score)
        if visible:
            fans1 += 1
print(fans1, max(scores))