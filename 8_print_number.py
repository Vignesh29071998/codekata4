n,q=map(int,input().split())
n1=list(map(int,input().split()))
q1,m=[],[]
flag=0
def gcd(m):
  mi=min(m)
  if len(m)==1:
    print(m[0])
  else:
    for i in range(mi,0,-1):
      for j in m:
        if j%i==0:
          g=i
          flag=1
        else:
          flag=0
          break
      if flag==1:
        print(g)
        break
      else:
        continue
for i in range(0,q):
  q1.append(list(map(int,input().split())))
for i in range(0,len(q1)):
  for j in range(q1[i][0],(q1[i][1])+1):
    m.append(n1[j-1])
  gcd(m)  
  m=[]
