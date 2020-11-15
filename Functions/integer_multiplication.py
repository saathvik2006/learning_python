def get_int(z):
	int(z)
	return z
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
x_input=input("What is your number? ")
y_input=input("What is your multiplier? ")
x=get_int(x_input)
y=get_int(y_input)
print (mult(x,y))