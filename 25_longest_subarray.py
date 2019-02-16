ip=int(input())
n1=list(map(int,input().split()))
m,n=1,0
for i in range(0,ip-1):
  if n1[i]<n1[i+1]:
    m+=1
  else:
    m=1
  if n<m:
    n=m
print(n)
