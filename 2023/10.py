import sys

stack = []
def cal(lr, lc, lval):
    global m

    stack.append((lr, lc, lval))

    while len(stack) > 0:
        r, c, val = stack.pop(0)

        if m[r][c][4] != 0 and val >= m[r][c][4]:
            continue
        m[r][c][4] = val
        #print(r, c, val)

        if r > 0 and m[r][c][0] and m[r-1][c][1]:
            stack.append((r-1, c, val+1))
        if r < len(m)-1 and m[r][c][1] and m[r+1][c][0]:
            stack.append((r+1, c, val+1))
        if c > 0 and m[r][c][2] and m[r][c-1][3]:
            stack.append((r, c-1, val+1))
        if c < len(m[0])-1 and m[r][c][3] and m[r][c+1][2]:
            stack.append((r, c+1, val+1))

def show(m, d):
    print('-----')
    for i in m:
        print([1 if j[d]!=0 else 0 for j in i])

def flood(m, dots, val):
    while len(dots) > 0:
        r, c = dots.pop(0)

        if m[r][c] != 0:
            continue
        m[r][c] = val


        if r > 0:
            dots.append((r-1, c))
        if r < len(m)-1 :
            dots.append((r+1, c))
        if c > 0:
            dots.append((r, c-1))
        if c < len(m[0])-1 :
            dots.append((r, c+1))

def is_loop_edge(lr, lc):
    if lr%2 == 0 and lc%2 == 0:
        return m[lr//2][lc//2][4] != 0
    if lr%2 == lc%2:
        return False
    if lr%2 == 1:
        if lc == 0 or lc == 2* (len(m[0]) - 1):
            return False
        if m[(lr-1)//2][lc//2][1] and m[(lr+1)//2][lc//2][0]:
            return True
    if lc%2 == 1:
        if lr == 0 or lr == 2* (len(m) - 1):
            return False
        if m[lr//2][(lc - 1)//2][3] and m[lr//2][(lc+1)//2][2]:
            return True

fans1 = 0
fans2 = 0
pitch = 0
m=[]

mt = {'|': [1, 1, 0, 0, 0],
      '-': [0, 0, 1, 1, 0],
      'L': [1, 0, 0, 1, 0],
      'J': [1, 0, 1, 0, 0],
      '7': [0, 1, 1, 0, 0],
      'F': [0, 1, 0, 1, 0],
      '.': [0, 0, 0, 0, 0],
      'S': [1, 1, 1, 1, 0]
      }

start_r=0
start_c=0
for line in sys.stdin:
   m.append([mt[c].copy() for c in line.strip()])
   c = line.find('S')
   if c != -1:
      start_c = c
      start_r = len(m) - 1

cal(start_r, start_c, 1)


fans1 = max(max(j[4] for j in i) for i in m)

#expand m
large_m=[]
for i in range(0, 2*len(m) - 1, 1):
    r = []
    for j in range(0, 2* len(m[0]) - 1, 1):
        r.append(1 if is_loop_edge(i, j) else 0)
    large_m.append(r)
#for i in large_m:
#    print(i)

#flood all the outside tiles
out_starts=[]
for i in range(0, len(large_m) - 1, 1):
    out_starts.append((i, 0))
    out_starts.append((i, len(large_m[0]) - 1 ))
for i in range(0, len(large_m[0]), 1):
    out_starts.append((0, i))
    out_starts.append((len(large_m) - 1, 0))


flood(large_m, out_starts, -1)

for i in range(0, len(m), 1):
    for j in range(0, len(m[0]), 1):
        if large_m[2*i][2*j] == 0:
            fans2 += 1

print('start ', start_r, start_c)
print(fans1 - 1, fans2)
