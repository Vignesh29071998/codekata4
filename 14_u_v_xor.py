n,q=map(int,input().split())
n1=list(map(int,input().split()))
a,s=[],[]
m=0
for i in range(0,q):
  a.append(list(map(int,input().split())))
for i in range(0,q):
  for j in range(a[i][0],(a[i][1])+1):
    s.append(n1[j-1])
  for i in range(0,len(s)-1):
    if i==0:
      m=s[i]^s[i+1]
    else:
      m=m^s[i+1]
  print(m)
  s=[]
  m=0
  
