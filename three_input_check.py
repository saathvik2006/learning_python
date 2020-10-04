first_input=int(input("Any number "))
second_input=int(input("2 number "))
third_input=int(input("3rd number "))
if first_input==second_input:
	if first_input==third_input:
		print ("All numbers are equal")
	else:
		print ("Not all numbers are equal")
else:
	print ("Not all of the numbers are equal")
if first_input==second_input or first_input==third_input or second_input==third_input:
	print ("Two of the numbers are equal")
else:
	print ("None of the numbers are equal")