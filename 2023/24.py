import sys
import math

from fractions import Fraction
vectors = []
for line in sys.stdin:
    l = line.strip().split(' @ ')
    vectors.append(([int(i) for i in l[0].split(', ')],
                   [int(i) for i in l[1].split(', ')]))

def count_inrange(l, r):
    c = 0

    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            ki = vectors[i][1][1] / vectors[i][1][0]
            kj = vectors[j][1][1] / vectors[j][1][0]
            li = vectors[i][1][2] / vectors[i][1][0]
            lj = vectors[j][1][2] / vectors[j][1][0]
            xi = vectors[i][0][0]
            xj = vectors[j][0][0]
            yi = vectors[i][0][1]
            yj = vectors[j][0][1]

            if kj == ki:
                if yj-yi == kj*(xj - xi):
                    # on the same line
                    c+=1
                # parallel
                continue
            xc = (yi-yj-xi*ki+xj*kj)/(kj-ki)
            yc = (xi-xj-yi/ki+yj/kj)/(1/kj-1/ki)
            if l <= xc <= r and l <= yc <= r:
                if (xc - xi) / vectors[i][1][0] >= 0 and \
                   (yc - yi) / vectors[i][1][1] >= 0 and \
                   (xc - xj) / vectors[j][1][0] >= 0 and \
                   (yc - yj) / vectors[j][1][1] >= 0:
                    c+=1
    return c
fans1 = count_inrange(200000000000000, 400000000000000)
print(fans1)
# It is very rare to have a solution for part2
# The way to approach is to find parallel lines.
# Track of the rock must be in the plane determined by the parallel lines.
# All the joint point of rock and hailstone are exactly the joint of the
# vector with the plane
# ...But unfortunately my input data contains no parallel vetors :(
# Never mind, choose any of the vectors and enum all the point on the first one,
# When meet the solution, all other vectors will accross the plane determined by
# the point and vector in a straight line

# Abort this solution implemention due to time complexity
'''
def dot_product(a, b):
    return [
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]
    ]
def determine_plane(spl_idx, spl_t, ref_idx):
    v1 = [vectors[spl_idx][0][x] + spl_t * vectors[spl_idx][1][x] - vectors[ref_idx][0][x] for x in range(3)]
    v2 = vectors[ref_idx][1]
    nv = dot_product(v1, v2)
    D = sum([nv[x]*vectors[ref_idx][0][x] for x in range(3)])
    return nv, D
def find_joint(plane, target_idx):
    nv = plane[0]
    D = plane[1]
    x = vectors[target_idx][0][0]
    y = vectors[target_idx][0][1]
    z = vectors[target_idx][0][2]
    vx = vectors[target_idx][1][0]
    vy = vectors[target_idx][1][1]
    vz = vectors[target_idx][1][2]
    if nv[0]*vx + nv[1]*vy + nv[2]*vz == 0:
        return 0, 0
    return (D - nv[0]*x - nv[1]*y - nv[2]*z)/(nv[0]*vx + nv[1]*vy + nv[2]*vz), \
        (D - nv[0]*x - nv[1]*y - nv[2]*z)%(nv[0]*vx + nv[1]*vy + nv[2]*vz)

def cal_point(v_idx, t):
    x = vectors[v_idx][0][0]
    y = vectors[v_idx][0][1]
    z = vectors[v_idx][0][2]
    vx = vectors[v_idx][1][0]
    vy = vectors[v_idx][1][1]
    vz = vectors[v_idx][1][2]
    return x+t*vx, y+t*vy, z+t*vz



for i in range(len(vectors)):
    for j in range(i, len(vectors)):
        x1 = vectors[i][0][0]
        y1 = vectors[i][0][1]
        z1 = vectors[i][0][2]
        vx1 = vectors[i][1][0]
        vy1 = vectors[i][1][1]
        vz1 = vectors[i][1][2]
        x2 = vectors[j][0][0]
        y2 = vectors[j][0][1]
        z2 = vectors[j][0][2]
        vx2 = vectors[j][1][0]
        vy2 = vectors[j][1][1]
        vz2 = vectors[j][1][2]
        # x1*vy2+t1*vx1*vy2 = x2*vy2+t2*vx2*vy2
        # y1*vx2+t1*vy1*vx2 = y2*vx2+t2*vy2*vx2
        #
        # (x1*vy1-y1*vx1 -x2*vy1 + y2*vx1) /(vx2*vy1-vy2*vx1)=t2


        if vx1*vy2!=vy1*vx2:
            t1 = Fraction(x2*vy2-y2*vx2-x1*vy2+y1*vx2,vx1*vy2-vy1*vx2)
            t2 = Fraction(x1*vy1-y1*vx1-x2*vy1+y2*vx1,vx2*vy1-vy2*vx1)
            if x1+t1*vx1 != (x2+t2*vx2):
                print('!!!', (x2*vy2-y2*vx2-x1*vy2+y1*vx2), (vx1*vy2-vy1*vx2), t1,(x1*vy1-y1*vx1-x2*vy1+y2*vx1),(vx2*vy1-vy2*vx1), t2)
            print (i, j, x1+t1*vx1-(x2+t2*vx2), y1+t1*vy1-(y2+t2*vy2), z1+t1*vz1-(z2+t2*vz2))

exit()
# construct parallel plane  Ax+By+Cz = D
BIG = 2**30
t0min = -1
t0max = -1
for i in range(2, len(vectors)):
    npl = determine_plane(0, 0, 1)
    tc, _ = find_joint(npl, i)
    print(tc)
    npl = determine_plane(i, 0, 1)
    tc, _ = find_joint(npl, 0)
    npl = determine_plane(i, 1, 1)
    tc1, _ = find_joint(npl, 0)
    npl = determine_plane(i, 2, 1)
    tc2, _ = find_joint(npl, 0)
    d1 = tc1 - tc
    d2 = tc2 - tc1
    if tc > 0:
        print(i, tc, tc1, tc2, d1, d2)
        if d1 > 0:
            t0min = max(t0min, tc) if t0min > 0 else tc
        else:
            t0max = min(t0max, tc) if t0max > 0 else tc

print(t0min, t0max)
exit()
nodes = []
c = math.floor(t0min)
while True:
    good = True
    pl = determine_plane(0, c, 1)

    # calculate the cross points
    badsolution = False
    for i in range(0, len(vectors)):
        t, m = find_joint(pl, i)
        if m > 0:
            good = False
            #print(c, t)
            break
        if t > 0:
            nodes.append((cal_point(i, t), t))
        #print(nodes)
    c += 1
    if not good:
        continue

    break
'''

def solve2(e):
    # a0x+b0y=c0
    # a1x+b1y=c1
    # a1a0x + a1b0y = a1c0
    # a0a1x + a0b1y = a0c1
    # => (a1b0-a0b1)y = a1c0-a0c1
    return Fraction(e[1][1]*e[0][2]-e[0][1]*e[1][2], e[1][1]*e[0][0]-e[0][1]*e[1][0]), \
           Fraction(e[1][0]*e[0][2]-e[0][0]*e[1][2], e[1][0]*e[0][1]-e[0][0]*e[1][1])
def solve3(e):
    # a0x+b0y+c0z=d0
    # a1x+b1y+c1z=d1
    # a1a0x + a1b0y + a1c0z = a1d0
    # a0a1x + a0b1y + a0c1z = a0d1
    # => (a1b0-a0b1)y + (a1c0-a0c1)z = a1d0-a0d1
    # => (a2b0-a0b2)y + (a2c0-a0c2)z = a2d0-a0d2
    eq2 = []
    for i in range(2):
        eq2.append(((e[i+1][0]*e[0][1]-e[0][0]*e[i+1][1]),
                    (e[i+1][0]*e[0][2]-e[0][0]*e[i+1][2]),
                    (e[i+1][0]*e[0][3]-e[0][0]*e[i+1][3])))
    y, z = solve2(eq2)
    x = (e[0][3] - e[0][1]*y - e[0][2]*z) / e[0][0]
    return x, y, z
    #
def solve4(e):
    # e0x+f0y+g0vx+h0vy=i0
    # e1x+f1y+g1vx+h1vy=i1
    # => e1e0x+e1f0y+e1g0vx+e1h0vy=e1i0
    #    e0e1x+e0f1y+e0g1vx+e0h1vy=e0i1
    # => (e1f0-e0f1)y + (e1g0-e0g1)vx + (e1h0-e0h1)vy = e1i0-e0i1
    eq3=[]
    for i in range(3):
        eq3.append(((e[i+1][0]*e[0][1]-e[0][0]*e[i+1][1]),
                    (e[i+1][0]*e[0][2]-e[0][0]*e[i+1][2]),
                    (e[i+1][0]*e[0][3]-e[0][0]*e[i+1][3]),
                    (e[i+1][0]*e[0][4]-e[0][0]*e[i+1][4]))
                   )
    y, vx, vy = solve3(eq3)
    x = (e[0][4] - e[0][1]*y - e[0][2]*vx - e[0][3]*vy)/e[0][0]
    return x, y, vx, vy
# Solution 2
# Rock(tx) = Hail_x(tx) where Rock(t)=(x+t*vx, y+t*vy, z+t*vz)
# Giving Hail_0 Hail_1 Hail_2 Hail_3 Hail_4
# Can find solution for (x, y, z, vx, vy, vz)

# Rock, Hail_0
#  * x+t0*vx = a0+t0*va0
#  * y+t0*vy = b0+t0*vb0
#  => t0 = (x-a0)/(va0-vx) = (y-b0)/(vb0-vy)
#  => (x-a0)(vb0-vy)= (y-b0)(va0-vx)
#  => x*vb0-x*vy-a0*vb0+a0*vy=y*va0-y*vx-b0*va0+b0*vx *1
# Rock, Hail_1:
#  => (x-a1)(vb1-vy)= (y-b1)(va1-vx)
#  => x*vb1-x*vy-a1*vb1+a1*vy=y*va1-y*vx-b1*va1+b1*vx *2
# *1, *2
#  => (vb0-vb1)*x-a0*vb0+a1*vb1+(a0-a1)*vy = (va0-va1)*y-b0*va0+b1*va1+(b0-b1)*vx
#  => (vb0-vb1)*x + (va1-va0)*y + (b1-b0)*vx + (a0-a1)*vy = b1*va1-b0*va0+a0*vb0-a1*vb1
#  => equation (vb0-vb1, va1-va0, b1-b0, a0-a1, b1*va1-b0*va0+a0*vb0-a1*vb1)
# Hail_2, Hail_3, Hail_4
#  => equation (vb0-vb2, va2-va0, b2-b0, a0-a2, b2*va2-b0*va0+a0*vb0-a2*vb2)
#  => equation (vb0-vb3, va3-va0, b3-b0, a0-a3, b3*va3-b0*va0+a0*vb0-a3*vb3)
#  => equation (vb0-vb4, va4-va0, b4-b0, a0-a4, b4*va4-b0*va0+a0*vb0-a4*vb4)

a, b, c, va, vb, vc = [], [], [], [], [], []
for i in range(5):
    a.append(vectors[i][0][0])
    b.append(vectors[i][0][1])
    c.append(vectors[i][0][2])
    va.append(vectors[i][1][0])
    vb.append(vectors[i][1][1])
    vc.append(vectors[i][1][2])
eq4=[]
for i in range(4):
    eq4.append((vb[0]-vb[i+1], va[i+1]-va[0], b[i+1]-b[0], a[0]-a[i+1],
               b[i+1]*va[i+1]-b[0]*va[0]+a[0]*vb[0]-a[i+1]*vb[i+1]))

x,y,vx,vy = solve4(eq4)
# (x-a0)(vc0-vz)= (z-c0)(va0-vx)
# => (x-a0)vc0 - (x-a0)vz = (va0-vx)z - c0(va0-vx)
#    (va0-vx)z + (x-a0)vz  = (x-a0)vc0 - (vx-va0)c0
# => (va1-vx)z + (x-a1)vz  = (x-a1)vc1 - (vx-va1)c1
z, vz = solve2([(va[i]-vx, x-a[i], (x-a[i])*vc[i] - (vx-va[i])*c[i]) for i in [0, 1]])

print(x+y+z)
