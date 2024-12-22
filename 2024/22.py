import sys

num=[]
for line in sys.stdin:
    num.append(int(line.strip()))

#print(num)

def cal(n):
    r = ((64 * n) ^ n)%16777216
    r = ((r // 32) ^ r)%16777216
    r = ((2048 * r) ^ r)%16777216
    return r

# s = 123
# for i in range(10):
#     s = cal(s)
#     print(s)
fans = 0
buyer = {}
turns = 2000
for n in num:
    s = n
    seq=[]
    for i in range(turns):
        s = cal(s)
        seq.append(s %10)
    fans += s
    buyer[n]=seq
print(fans)

#part2
monkey = {}
for n in num:
    sub_mon = {}
    for i in range(3, turns):
        if i == 3:
            x = n%10
        else:
            x = buyer[n][i-4]
        key=(buyer[n][i-3] - x, buyer[n][i-2] - buyer[n][i-3], buyer[n][i-1] - buyer[n][i-2], buyer[n][i] - buyer[n][i-1])
        if key not in sub_mon:
            sub_mon[key] = buyer[n][i]
    for k in sub_mon:
        if k not in monkey:
            monkey[k] = sub_mon[k]
        else:
            monkey[k] += sub_mon[k]

print(max([monkey[k] for k in monkey]))


