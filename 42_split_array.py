n,k = map(int,input().split())
l = list(map(int,input().split()))
a,b,ma = [],[],[]
def split(a,m):
  mi = 0
  for i in range(0,m):
    mi = min(a[i])
    b.append(mi)
  ma.append(max(b))
  return ma
if k ==1 or n==k:
  print(min(l))
else:
  for i in range(0,n-1):
    for j in range(0,k):
      if j%2==0:
        a.append(l[:i+1])
      else:
        a.append(l[i+1:])
    b = []
    c = split(a,k)
    a = []
  print(max(c))
