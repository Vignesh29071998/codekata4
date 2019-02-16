a=int(input())
i=0
c=0
b=[]
while i<90 and i<a:
  s=0
  for j in str(a-i):
    s+=int(j)
  if s+(a-i)==a:
    c+=1
    b.append(a-i)
  i+=1
print(c)
for i in b:
  print(i)
