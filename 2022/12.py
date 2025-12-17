import sys
import math

fmap = []
score = []
score2 = []

sr, sc = (0, 0)
er, ec = (0, 0)


for i,line in enumerate(sys.stdin):
    l = line.strip()
    nl = []
    for j, c in enumerate(l):
        if c == 'S':
            sc = j
            sr = i
            nl.append(0)
        elif c == 'E':
            ec = j
            er = i
            nl.append(25)
        else:
            nl.append(ord(c) - ord('a'))
    fmap.append(nl)
    score.append([-1]*len(nl))
    score2.append([-1]*len(nl))

score[sr][sc] = 0
score2[sr][sc] = 0
stk = [(sr, sc, score[sr][sc])]

dmap = [(-1, 0), (0, -1), (0, 1), (1, 0)]
while len(stk):
    cr, cc, cd = stk.pop()
    for di in dmap:
        nr = cr + di[0]
        nc = cc + di[1]
        if nr < 0 or nr >= len(fmap):
            continue
        if nc < 0 or nc >= len(fmap[0]):
            continue
        if fmap[nr][nc] == fmap[cr][cc] + 1 or fmap[nr][nc] <= fmap[cr][cc]:
            if score[nr][nc] < 0 or score[nr][nc] > cd + 1:

                score[nr][nc] = cd + 1
                stk.append((nr, nc, score[nr][nc]))
stk = [(sr, sc, score2[sr][sc])]
while len(stk):
    cr, cc, cd = stk.pop()
    for di in dmap:
        nr = cr + di[0]
        nc = cc + di[1]
        if nr < 0 or nr >= len(fmap):
            continue
        if nc < 0 or nc >= len(fmap[0]):
            continue
        if fmap[nr][nc] == fmap[cr][cc] + 1 or fmap[nr][nc] <= fmap[cr][cc]:
            if fmap[nr][nc] == 0:
                nv = 0
            else:
                nv = score2[cr][cc] + 1
            if score2[nr][nc] < 0 or score2[nr][nc] > nv:
                score2[nr][nc] = nv
                stk.append((nr, nc, score2[nr][nc]))

print(score[er][ec], score2[er][ec])

