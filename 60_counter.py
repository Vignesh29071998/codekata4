n = int(input())
a = []
b,i,j = 3,1,1
while i < 100001:
  c = b
  while j < b+i:
    a.append([j,c])
    c -=1
    j +=1
  i = b+i
  j = i
  b = b*2
for i in range(0,len(a)):
    if a[i][0] == n:
      print(a[i][1])
      break

