a=int(input())
s=0
if int(a**(1/2))==a**(1/2):
  print(s)
else:
  for i in range(a,0,-1):
    if int(i**(1/2))==i**(1/2):
      print(s)
      break
    else:s+=1
    
