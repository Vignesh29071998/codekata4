a,b,f,k = map(int,input().split())
flag=0
for i in range(0,k):
  if abs(0-f)*2 <=b and abs(f-a)*2<=b:
    flag=1
  else:
    flag=0
    break
if flag==1:
  print(k)
else:
  print('-1')
