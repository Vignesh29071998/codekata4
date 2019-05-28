n,w = map(int,input().split())
value = list(map(int,input().split()))
weight = list(map(int,input().split()))
c,m = 0,0
for i in range(0,n-1):
  for j in range(i+1,n):
    for k in range(i+1,n-j+1):
      su = value[i]+sum(value[k:k+j])
      m = weight[i]+sum(weight[k:k+j])
      if su <= w and m>c:
        c = m
print(c)
