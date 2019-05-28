n,w = map(int,input().split())
value = list(map(int,input().split()))
weight = list(map(int,input().split()))
c,m,p = 0,0,1
for i in range(0,n-1):
  for j in range(i+1,n):
    for k in range(i+1,n-j+p):
      su = value[i]+sum(value[k:k+j])
      m = weight[i]+sum(weight[k:k+j])
      if su <= w and m>c:
        c = m
  p += 1
print(c)
