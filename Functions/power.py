def mult(x,y):
  counter=1
  product=0
  while counter<=y:
    product+=x
    counter+=1
  return product
a=int(input("What is your number? "))
b=int(input("What do you want to raise it to? "))
def power(m,n):
  counter=1
  result=1
  while counter<=n:
    result=mult(result,m)
    counter+=1
  return result
print (power(a,b))