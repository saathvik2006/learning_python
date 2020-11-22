def favorite_word():
	word=input("What is your favorite word? ")
	return word
def favorite_number():
	number=int(input("What is your favorite number? "))
	return number
def loopy():
	word=favorite_word()
	number=favorite_number()
	counter=1
	while counter<=number:
		print (word)
		counter+=1
loopy()
	