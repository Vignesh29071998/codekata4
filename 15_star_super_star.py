n=int(input())
n1=list(map(int,input().split()))
s=[]
for i in range(0,n-1):
  if n1[i]>max(n1[i+1:]):
    s.append(n1[i])
s.append(n1[n-1])
print(*s)
print(max(n1))
    
