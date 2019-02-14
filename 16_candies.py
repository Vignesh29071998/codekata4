n=int(input())
n1=list(map(int,input().split()))
candy=len(n1)
for i in range(0,len(n1)-1):
  if n1[i]<n1[i+1]:
    candy+=n1[i]
print(candy)
