password=input("Please create a new password\na.Yourpassword must be at least 8 characters long.\nb.Your password must only consist of letters and digits\nc.Your password must contain at least 2 digits.\n")
def is_valid(the_password):
	num_characters=len(the_password)
	if num_characters<8:
		print("Not a valid password! Passwords must be at least 8 characters long.")
		valid=False
		return valid
	num_digits=0
	for i in the_password:
		if (i.isdigit()):
			num_digits+=1
		elif (i.isalpha()):
			continue
		else:
			print("Not a valid password! Passwords must only contain letters or digits")
			valid=False
			return valid
	if num_digits>=2:
		print ("Valid password")
	else:
		print("Not a valid password! Passwords must contain at least 2 digits")
		valid=False
		return valid
is_valid(password)
