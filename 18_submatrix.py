n,m = map(int,input().split())
a,b,c,d,e = [],[],[],[],[]
for i in range(0,n):
  a.append(list(map(int,input().split())))
if m != 1:
  for x in range(0,n-1):
    for i in range(0,n-1):
      for j in range(0,m-1):
        for k in range(0,j+2):
          for l in range(0,j+2):
            try:
              b += [a[k+i][l+x]]
            except IndexError:
              b = []
              break
        c.append(b)
        b = []
  for i in c:
    if 0 in i or i==[]:
      continue
    else:
      d.append(i)
  if d==[]:
    print(1)
  else:
    p = max(d)
    for i in range(0,int(len(p)**(1/2))):
      for j in range(0,int(len(p)**(1/2))):
        e.append(1)
      print(*e)
      e = []
else:
  print(1)
