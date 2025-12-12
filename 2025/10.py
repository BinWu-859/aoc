import sys
from xml.parsers.expat import model
import numpy as np
import z3

def found_pattern(leds, buttons):
    new_leds = []
    for led in leds:
        for b in buttons:
            new_led = led.copy()
            #print(b, new_led)
            for i in b:
                new_led[i] = not new_led[i]
            #print('->',b, new_led)
            if not any(new_led):
                return True, []
            new_leds.append(new_led)
        #print(new_leds)
    return False, new_leds

ans1 = 0
ans2 = 0
line_c = 0
for line in sys.stdin:
    buttons = []
    jol = []
    t1 = line.strip().split(']')
    led = []
    line_c += 1
    for c in t1[0][1:]:
        if c == '.':
            led.append(False)
        else:
            led.append(True)
    t2 = t1[1].strip().split(' {')
    t3 = t2[0].split(' ')
    for c in t3:
        buttons.append(list(map(int, c[1:-1].split(','))))
    t4 = t2[1][:-1].split(',')
    jol.extend(list(map(int, t4)))
    #print(led, button, jol)

    count = 0
    newleds = [led]
    while True:
        found, newleds = found_pattern(newleds, buttons)
        count += 1
        if found:
            break
    ans1 += count

    count = 0

    solver = z3.Solver()
    xs = []
    for n in range(len(buttons)):
        x = z3.Int(f"x{n}")
        xs.append(x)
        solver.add(x >= 0)

    #print(xs)

    for i, r in enumerate(jol):
        p = []
        for j, c in enumerate(buttons):
            if i in c:
                p.append(xs[j])

        solver.add(z3.Sum(p) == r)
    #print(solver)
    count = 0
    while solver.check() == z3.sat:
        count = 0
        m = solver.model()
        for i in m:
            count += m[i].as_long()
        solver.add(z3.Sum(xs) < count)

    ans2 += count

print(ans1, ans2)

