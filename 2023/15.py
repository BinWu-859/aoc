import sys

def myhash(s):
    v = 0
    for i in s:
        v += ord(i)
        v *= 17
        v %= 256
    return v

def handle(boxes, s):
    if s[-1] == '-':
        label = s[:-1]
        box = myhash(label)
        #print(label, box)
        if box in boxes:
            for i in boxes[box]:
                if i[0] == label:
                    boxes[box].remove(i)
    else:
        t = s.split('=')
        label = t[0]
        v = int(t[1])
        box = myhash(label)
        #print(label, box)
        if box not in boxes:
            boxes[box] = [[label, v]]
        else:
            found = False
            for i in boxes[box]:
                if i[0] == label:
                    i[1] = v
                    found = True
            if not found:
                boxes[box].append([label, v])
    #print(s, boxes)

def calc(boxes):
    v = 0
    for box in boxes:
        #print(box)
        for i, k in enumerate(boxes[box]):
            #print(i, k)
            v += (box + 1) * (i + 1) * k[1]
    return v

ans1 = 0
ans2 = 0
boxes={}
for line in sys.stdin:
    data = line.strip().split(',')
    for s in data:
        ans1 += myhash(s)
        handle(boxes, s)



print(ans1, calc(boxes))


