n,k = map(int,input().split())
k1 = [10,20,40,80,160,320,640,1280]
c = 0
if k == 0 or k==1:
  print(n)
else:
  a = n*k1[k-1]
  b = n*10**k
  if a%n == 0:
    c = str(a)
    for i in c:
      if i=='0':
        c = c+1
      else:
        c =0
    if c>=len('0'*k):
      print(a)
    else:
      print(n*10**k)
