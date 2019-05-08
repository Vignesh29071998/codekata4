n,k=map(int,input().split())
n1=list(map(int,input().split()))
n1=sorted(n1)
team,i=0,0
flag=0
while i<len(n1)-2:
  a,b,c=n1[i:i+3]
  for j in range(0,k):
    a,b,c=a+1,b+1,c+1 
    if a<=5 and b<=5 and c<=5:
      flag=1
    else:
      flag=0
  if flag==1:
    team+=1
  i+=3
  a,b,c=0,0,0
print(team)
