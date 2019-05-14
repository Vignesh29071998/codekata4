a = input()
b = input()
c = a.split('|')
if len(c[0]+b)==len(c[1]):
  print(c[0]+b+'|'+c[1])
elif len(c[0])==len(c[1]+b):
  print(c[0]+'|'+c[1]+b)
else:
  print("Impossible")
