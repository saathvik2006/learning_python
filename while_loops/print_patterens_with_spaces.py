number = 
i=1
j=number//2
while i>=1:
  a = " "*j + "*"*i + " "*j
  print(a)
  i+=2
  j-=1
  if i>number:
    break
i= number-2
j= 1
while i>=1:
  a = " "*j + "*"*i + " "*j
  print(a)
  i-=2
  j+=1