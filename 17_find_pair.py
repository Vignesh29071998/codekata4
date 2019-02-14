a,b=map(int,input().split())
l=list(map(int,input().split()))
flag=0
for i in range(0,len(l)-1):
  if l[i]+l[i+1]==b:
    flag=1
    break
  else:
    flag=0
if flag==1:
  print('yes')
else:
  print('no')
