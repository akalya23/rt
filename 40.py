num1=int(input())
a=0
b=1
for i in range(num1):
  print(b,end=' ')
  c=b+a
  a,b=b,c
