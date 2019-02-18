n,s=map(int,input().split())
n1=list(map(int,input().split()))
n1=sorted(n1,reverse=True)
c=0
while s>0:
  for i in range(0,n):
    if s>=n1[i]:
      s-=n1[i]
      c+=1
      break
print(c)
