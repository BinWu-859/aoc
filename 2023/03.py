import sys

class painter:
    def __init__(self, origin):
        self.pallet = []
        self.origin = origin
        for i in origin:
            self.pallet.append(self.color(i))
        self.i_pitch = len(origin)
        self.j_pitch = len(origin[0])
        print(self.i_pitch, self.j_pitch)
    def color(self, line):
        ret = []
        for c in line:
            if c == '.':
                ret.append(0)
                continue
            if c == '*':
                ret.append(5)
                continue
            if c.isdigit():
                ret.append(1)
                continue
            ret.append(2)
        return ret
    def mark(self, i , j, pos):
        if i < 0 or i >= self.i_pitch:
            return
        if j < 0 or j >= self.j_pitch:
            return
        if self.pallet[i][j] == 1:
            self.pallet[i][j] = pos * 10 + 3
            self.mark(i, j-1, pos)
            self.mark(i, j+1, pos)
    def paint(self, gear):
        for i, l in enumerate(self.pallet):
            for j, c in enumerate(l):
               if (c == 2 and not gear) or c == 5:
                   pos = i * self.j_pitch + j
                   self.mark(i - 1, j - 1, pos)
                   self.mark(i - 1, j, pos)
                   self.mark(i - 1, j + 1, pos)
                   self.mark(i, j - 1, pos)
                   self.mark(i, j + 1, pos)
                   self.mark(i + 1, j - 1, pos)
                   self.mark(i + 1, j, pos)
                   self.mark(i + 1, j + 1, pos)
        for i, l in enumerate(self.pallet):
            print(l)
    def ans01(self):
        self.paint(False)
        ans = 0
        for i, l in enumerate(self.pallet):
            tl = ''
            for j, c in enumerate(l):
                if c%10 != 3:
                    tl = tl + ' '
                else:
                    tl = tl + self.origin[i][j]
            nl = tl.split()
            for n in nl:
                ans = ans + int(n)
        return ans
    def ans02(self):
        self.paint(True)
        ans = 0
        gears = {}
        for i, l in enumerate(self.pallet):
            tmp = 0
            lc = 0
            for j, c in enumerate(l):
                if c%10 == 3:
                    tmp = tmp * 10 + int(self.origin[i][j])
                    lc = c
                if (c%10 != 3 or j == self.j_pitch - 1) and lc != 0:
                    if lc in gears:
                        ans = ans + tmp * gears[lc]
                        print('match {} with gear[{}]'.format(tmp, lc))
                        lc = 0
                        tmp = 0
                    else:
                        gears[lc] = tmp
                        print('gear[{}] = {}'.format(lc, tmp))
                        tmp = 0
                        lc = 0
        return ans


fans1 = 0
fans2 = 0
origin=[]

for line in sys.stdin:
    sline = line.rstrip()
    if '' == sline:
        break
    origin.append(sline)

p = painter(origin)
fans1 = p.ans01()
fans2 = p.ans02()

print(fans1, fans2)

