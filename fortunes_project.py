fortunes=["A beautiful, smart, and loving person will be coming into your life.",
"A dubious friend may be an enemy in camouflage.",
"A faithful friend is a strong defense.","A fresh start will put you on your way.",
"A friend asks only for your time not your money.",
"A friend is a present you give yourself.",
"A golden egg of opportunity falls into your lap this month.",
"A lifetime of happiness lies ahead of you.",
"A light heart carries you through all the hard times",
"A pleasant surprise is waiting for you."]
def get_name():
	name=input("What is your name? ")
	one=len(name)
	return one
def get_month():
	month=input("What month were you born in? ")
	two=len(month)
	return two
def get_color():
	color=input("What is your favorite color? ")
	three=len(color)
	return three
def ask_questions():
	sum=get_name()+get_month()+get_color()
	return sum
def get_fortune():
	return_value=ask_questions()
	index=return_value%len(fortunes)
	print (fortunes[index])
get_fortune()