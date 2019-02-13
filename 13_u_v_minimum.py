#hello this is my code
n,q=map(int,input().split())
n1=list(map(int,input().split()))
a=[]
s=[]
for i in range(0,q):
  a.append(list(map(int,input().split())))
for i in range(0,q):
  for j in range(a[i][0],(a[i][1])+1):
    s.append(n1[j-1])
  print(min(s))
  s=[]
