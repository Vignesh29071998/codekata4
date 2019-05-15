a = input()
b,c,flag,count = '',[],0,0
for i in range(0,len(a)-1):
  count +=1
  j = 0
  while j < len(a)-i:
    if j!=len(a)-i-1:
      b = a[j:j+i+1]
      c.append(b)
      j = j+1
    else:
      c.append(a[j:j+i+1])
      j = j+1
  l = c[0]
  for i in range(0,len(l)):
    for j in range(1,len(c)):
      if c[0][i] in c[j]:
        flag = 1
      else:
        flag = 0
        break
    if flag == 1:
      print(count)
      break
    else:
      continue
  c = []
  if flag==1:
    break  

