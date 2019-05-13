a,b,f,k = map(int,input().split())
c,gas = 0,b
l = abs(0-f)
gas = gas-l
for i in range(1,k+1):
  if i%2!=0:
    if i==k:
      if abs(f-a) > gas:
        c = c+1
    elif abs(f-a)*2 > gas:
      gas = b-abs(f-a)*2
      c = c+1
    else:
      gas = gas-abs(f-a)*2
  elif i%2==0:
    if i==k:
      if abs(0-f) > gas:
        c = c+1
    elif abs(0-f)*2 > gas:
      gas = b-abs(0-f)*2
      c = c+1
    else:
      gas = gas-abs(0-f)*2
if gas < 0:
  print('-1')
else:
  print(c)
  
