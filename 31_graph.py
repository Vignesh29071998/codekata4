a,b=map(int,input().split())
a1,b1,su,su1,m=[],[],0,[],0
for i in range(0,a):
  a1.append(list(map(int,input().split())))
b1=[x for x in a1 if x!=[]]
for i in range(0,len(b1)):
  if b1[i][0]==1:
    m+=1
b1=sorted(b1)
for i in range(0,m):
  if b1[i][0]==1:
    su+=1
    su+=b1[i][1]
    v=b1[i][1]
    for j in range(m,len(b1)):
      if v==b1[j][0]:
        su+=b1[j][1]
        v=b1[j][1]
  su1.append(su)
  v,su=0,0
print(max(su1))
