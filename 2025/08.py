import sys
import math

def distant(box1, box2):
    return math.sqrt(sum((int(a) - int(b)) ** 2 for a, b in zip(box1, box2)))

def solve(num):
    part1 = 0
    part2 = 0
    boxes = []
    for line in sys.stdin:
        boxes.append(tuple(line.strip().split(',')))
    map = []
    for i in range(len(boxes) - 1):
        for j in range(i+1, len(boxes)):
            map.append((i, j, distant(boxes[i], boxes[j])))
    map.sort(key=lambda x: x[2])
    groups = {}
    boxes_group = {}
    new_group = 1
    for i in range(len(boxes)):
        boxes_group[i] = new_group
        groups[new_group] = [i]
        new_group += 1

    count = 0
    for m in map:
        if part1 == 0 and count >= num:
            ans_count = []
            for g in groups:
                ans_count.append(len(groups[g]))
            ans_count.sort(reverse=True)
            part1 = ans_count[0]*ans_count[1]*ans_count[2]
            if part2 > 0:
                return (part1, part2)
        count += 1
        i, j, dist = m
        if boxes_group[i] != boxes_group[j]:
            og = boxes_group[j]
            for b in groups[boxes_group[j]]:
                boxes_group[b] = boxes_group[i]
            groups[boxes_group[i]].extend(groups[og])
            groups.pop(og)
        if part2 == 0 and len(groups) == 1:
            part2 = int(boxes[i][0]) * int(boxes[j][0])
            if part1 > 0:
                return (part1, part2)

    return (part1, part2)

print(solve(1000))