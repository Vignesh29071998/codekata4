n=int(input())
n1=list(map(int,input().split()))
c=0
for i in range(0,n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      if n1[i]<n1[j]<n1[k]:
        c+=1
print(c)        
        
