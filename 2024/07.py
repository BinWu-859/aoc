import sys

fans1, fans2 = 0, 0

# Time wasted on handling priority
# left-to-right being ignored :(
# def calc(l, ops):
#     plus=0
#     temp = l[0]
#     print(l, ops, temp+plus)
#     for i in range(1, len(l)):
#         if ops%2 == 1:
#             temp *= l[i]
#         else:
#             plus += temp
#             temp = l[i]
#         print(temp, plus)
#         ops = ops//2
#     print(l, ops, temp+plus)
#     return temp + plus
def calc(l, ops, n):
    temp = l[0]
    for i in range(1, len(l)):
        if ops%n == 1:
            temp *= l[i]
        elif ops%n == 0:
            temp += l[i]
        else:
            count = 0
            t = l[i]
            while t > 0:
                count+=1
                t = t//10
            temp = temp*10**count + l[i]
        ops = ops//n
    #print(l, ops, temp)
    return temp


def cal(r, l, n):

    ops = len(l) - 1
    for i in range(n**ops):
        if r == calc(l, i, n):
            return True
    return False


for line in sys.stdin:
    l = line.strip().split(': ')
    ans = int(l[0])
    num = [int(i) for i in l[1].split()]

    if cal(ans, num, 2):
       fans1 += int(l[0])
    if cal(ans, num, 3):
       fans2 += int(l[0])
print(fans1, fans2)
