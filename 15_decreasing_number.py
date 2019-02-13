a=int(input())
b=list(map(int,input().split()))
for i in range(0,len(b)-1):
  for j in range(i+1,len(b)):
    m,n=bin(b[i]),bin(b[j])
    m1,n1=0,0
    for k in m:
      if k=='1':
        m1+=1
    for l in n:
      if l=='1':
        n1+=1
    if m1<=n1:
      if b[i]<b[j]:
        b[i],b[j]=b[j],b[i]
for i in b:
  print(i)
    
  
