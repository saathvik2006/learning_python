def print_word(word,num):
  counter=1
  while counter<=num:
    print(word)
    counter+=1
input_word=input("What is your word? ")
input_number=int(input("What is your number? "))
print_word(input_word,input_number)