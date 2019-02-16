a=input()
flag=0
for i in range(1,len(a)):
  j=0
  while j<len(a) and len(a[:j]+a[i+j:])==len(a)-i:
    n=a[:j]+a[j+i:]
    if int(n)%8==0:
      flag=1
      print('yes')
      break
    j+=1
  if flag==1:
      break
else:
  print('no')
    
    
    
    
  
  
        
      
  
