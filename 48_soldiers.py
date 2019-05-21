n = int(input())
l, c = [], 0
for i in range(0, n):
  l.append(list(map(int, input().split())))
def fact(a,b):
  m = 1
  for k in range(b+1,a+1):
    m = m*k
  return m
for i in l:
  x = fact(i[0],i[1])
  while x > 1:
    for i in range(2, 10000000):
      if x % i == 0:
        p = i
        break
    x = x//p
    c += 1
  print(c)
  c = 0
