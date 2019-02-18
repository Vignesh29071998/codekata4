s=input()
flag=0
for i in range(0,len(s)-1):
  for j in range(i+1,len(s)):
    if s[i]<s[j]:
      flag=1
      print(s[j:])
      break
  if flag==1:
    break
else:
  print(s)
