def is_true():
	if x:
		print ("Congratulations!")
number=int(input("Input a number 0 or 1? "))
while number!=1 and number!=0:
	number=int(input("Try again "))
if number==0:
  x=True
else:
  x=False
is_true()