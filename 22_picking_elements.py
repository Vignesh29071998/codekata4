n = int(input())
li = list(map(int,input().split()))
su = 0
ma = 0
for i in range(0,n-1):
  for j in range(i,n,2):
    su = su+li[j]
  if su > ma:
    ma = su
  su = 0
print(ma)
