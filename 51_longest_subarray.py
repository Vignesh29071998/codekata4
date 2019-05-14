n = int(input())
c,b = 1,[]
l = list(map(int,input().split()))
for i in range(0,n-1):
  for j in range(i,n-1):
    if (l[j] < 0 and l[j+1]>0) or (l[j]>0 and l[j+1]<0):
      c = c+1
    else:
      break
  b.append(c)
  c = 1
b.append(c)
print(*b)
