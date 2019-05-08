a=input()
b=list(map(int,input().split()))
su=0
for i in range(1,len(b)-1):
  if b[i]<b[i+1] and b[i]<b[i-1]:
    su+=1
  elif b[i]>b[i+1] and b[i]>b[i-1]:
    su+=1
print(su)
