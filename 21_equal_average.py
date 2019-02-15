n=int(input())
n1=list(map(int,input().split()))
a1,a2=[],[]
for i in range(0,n-1):
    a1=n1[:i+1]
    a2=n1[i+1:]
    if sum(a1)//len(a1)==sum(a2)//len(a2):
      print('yes')
      break
else:
  print('no')
