def mult(x,y):
  counter=1
  product=0
  while counter<=y:
    product+=x
    counter+=1
  return product
a=int(input("What is your number? "))
b=int(input("What do you want to multiply by? "))
print (mult(a,b))