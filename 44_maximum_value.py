n,p,q,r = map(int,input().split())
a = list(map(int,input().split()))
ma=0
for i in range(0,n):
  for j in range(i,n):
    for k in range(j,n):
      if i<=j<=k:
        c = p*a[i] + q*a[j] + r*a[k]
        if c > ma:
          ma = c
print(ma)

  
