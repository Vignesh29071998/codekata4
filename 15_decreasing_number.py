a=int(input())
b=list(map(int,input().split()))
c=sorted(b,reverse=True)
for i in c:
  print(i)
