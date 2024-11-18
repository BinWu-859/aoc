import sys



def ans01(str):
  ans = 0
  for c in str:
    if c.isdigit():
        ans = int(c) * 10
        break
  for c in reversed(str):
    if c.isdigit():
        ans = ans + int(c)
        break
  return ans

fans = 0
for line in sys.stdin:
    if '' == line.rstrip():
        break
    tans = ans01(line)
    #print(tans)
    fans = fans + tans
print(fans)

