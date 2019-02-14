a,b=map(int,input().split())
l=list(map(int,input().split()))
flag=0
for i in range(0,len(l)-1):
  for j in range(i+1,len(l)):
    if l[i]+l[j]==b:
      flag=1
      break
    else:
      flag=0
  if flag==1:
    print('yes')
    break
else:
  print('no')
