my_list = ["a", "b", "c", "d", "e", "f", "g"]
index = 0
length = len(my_list) # length = 7
while index<length: # index starts from 0, ends at 6 , index<7
  if(my_list[index] == 'e'): # my_list[6] is "g"
    break
  else:
    print(my_list[index])
  index+=1