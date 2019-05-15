n,k = map(int,input().split())
k1 = [10,20,40,80,160,320,640,1280]
if k == 0:
  print(n)
else:
  a = n*k1[k-1]
  b = n*10**k
  if a%n == 0:
    c = str(a)
    if c[-k:]=='0'*k:
      print(a)
    else:
      print(n*10**k)
