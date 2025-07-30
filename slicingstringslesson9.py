name = "Harry, Alia, Arya"
character = name[0 : 5]
another_character = name[ : 5]
print(character)
print(another_character)


# find length of any string i.e total number of characters
length_ = "any name is what"
print(len(length_))
print(length_[0: -10]) 
print(length_[-15 : -10])
print(length_[0:4]) #including zero but not 4
print(length_[1:4]) #including 1 but not 4

# when using negative slicing python "minus" the number like this i.e
# length_[-3: -10] total length of this string is 16, this is going to happen
# 16-3 = 13, 16-10 = 6 it will be length[ 13 : 6] lets check the result in bpth ways


''' Print the first 4 characters of "Programming is fun".'''
# making a variable is_fun 
is_fun = "Programming is fun"
# slicing and printing first 4 characters Prog
print(is_fun[0 : 4])


'''Print characters from index 3 to 9 from "Welcome to Earth".'''
# Creating str() variable welcome
welcome = "Welcome to Earth"
# printing characters from 3 to 9, which should result in "come to" 
# wrong please remember 9 is not counted it will print only "come t"
print(welcome[3 : 9])


'''Print everything from the beginning to index 6 (not included) in "PythonPower".'''
# creating a variable name beg_to_6
beg_to_6 = "PythonPower"
# Printing from 0 to 6 included, result should be "PythonP" using indexing
print(beg_to_6[0:7])



'''Slice from index 2 to second last character of "Supercoder".'''
# creating variable two_to_last 
two_to_last = "Supercoder"
# printing using index [0 : 9] using indexing result should be "Supercode"
print(two_to_last[0 : 9])



'''Use slicing to remove the first word from "Code with me".'''
# Creating variable removefirst
removefirst = "Code with me"
# calculating length of string with len() function
print(len(removefirst)) # 12
# remove the first word, i will just slice it out by indexing using [4 : 12] and print() result should be " with me"
print(removefirst[4 : ]) # it will print the left automatically
print(removefirst[4 : 12]) # now i hardcoded this value





'''Print the last 5 characters of "NeverGiveUp".'''
# creating variable never_giveup
never_giveup = "NeverGiveUp"
# now printing length with len()
print(len(never_giveup)) # 12
# indexing with [-5 : ] it should print "iveup"
print(never_giveup[-5 : ])
print(never_giveup[-5: None])   #  Also works (None means “go till the end”)
print(never_giveup[-5:len(never_giveup)])  #  Also valid




'''Print characters from -8 to -3 from "Understanding".'''
# creatng variable understanding
understanding = "Understanding"
# now printing as the challenge requested from [-8 : -3] should print "stand"
# -3 will not be in the result which is "i"
print(understanding[-8 :-3])





'''Print everything except the last character from "Goodbye!".'''
# creating variable bye
bye = "Goodbye!"
# finding length with len()
print(len(bye)) #8, length function start counting from 1 not zero(0)
# printing as [0 : 7] it should print without the last letter
print(bye[0 : 7])



'''Reverse a string using slicing only (no loops).'''
# creating a variable with some string
convert = "String"
# using negative indexing and printing [-1 : -7] output can be reverse not worked
# printing each with its index place
print(convert[-1] + convert[-2] + convert[-3] + convert[-4] + convert[-5] + convert[-6])

# [5 :: -1 ]This means: Start from index 5 (last letter), 
# move backward one step at a time until the beginning, and print each character.
print(convert[6 :: -1])



'''Slice from index -3 to -10 from "Inspiration123" (then confirm with length trick).'''
# creating variable from_threeto_10
from_threeto_10 = "Inspiration123"
# slicing as requested in the problem
print(from_threeto_10[-3 : -10])  #Default slicing is left-to-right (step=1), so it's empty

# Start at index -3, move backward with step -1,
#  and stop before index -10 — printing characters in reverse.
print(from_threeto_10[-3 : -10 : -1])
# checking with lenght len()
print(len(from_threeto_10))




'''Print the whole string using [:] from "MagicSpell" and confirm it’s identical.'''
# creating variable identical
identical = "MagicSpell"
# printing as [:] output as said should be identical
print(identical[ : ]) #correct result



'''Slice the string in a way that returns empty string from "Challenge".'''
# craeting variable empty
empty = "Challenge"
# using this [-1 : -9] it will start from -1 and will stop there because this can't go back,
#  because it just go on until you don't specifaclly tell it to go backward.
print(empty[-1 : -9]) # empty achieved




'''Print every character except the first one from "Hello World".'''
# making variable greeting
greeting = "Hello World"
# now slicing [1 : ] this will leave "H" and print the rest result = ello World
print(greeting[1 : ]) # result achieved




'''Print every character except the last one from "PracticeMakesPerfect".'''
# creating variable last_one_excluded
last_one_excluded = "PracticeMakesPerfect"
# now getting length or number of digits using len()
print(len(last_one_excluded)) # 20 result, in listing from zero it's 0 to 19
# now printing [0 : 19] should print "PracticeMakesPerfec"
print(last_one_excluded[0 : 19])
print(last_one_excluded[:-1])  # Same result




'''Slice to only get the middle part of "Machine Learning" → "ine Lear".'''
# making variable middle
middle = "Machine Learning"
# [4 : 12 ] should print "ine Lear"
print(middle[4 : 12])




'''
text = "Visualizing"

Print characters from index len(text)-7 to len(text)-2.
'''

# making variable commanded
commanded = "Visualizing"
# as assigned in the statemen len(text)-7 to len(text)-2
# assigning them in variables as each seperately and will be joined in print
seven_len = len(commanded)-7
two_len = len(commanded)-2
# printing result
print(commanded[seven_len : two_len])



'''Use slicing to get "Python" from "ILovePythonALot" without counting manually.'''
# making variable release_it
relese_it = "ILovePythonALot"
# print as [5 : 11] expected result = Python
print(relese_it[5 : 11])


'''Given sentence = "Programming is life", use len() and negative slicing to get "life".'''
# making variable life
life = "Programming is life"
# printing as [-4 : ] should print life
print(life[-4:])



'''Loop through every sliced part (first 5 chars) of "AmazingWorld" and print each character.'''
# making variable = looping
looping = "AmazingWorld"
# printing every character in new line while looping with lep as variable target variable looping. 
for lep in looping[0:5]:
    # printing variable lep
    print(lep)
# slicing variable looping in looped
looped = looping[0:5]
# creating an empty container for holding characters from for loop
count = ""
# getting into for loop as loopin target variable is looping
for loopin in looped:
    count = count + loopin
# printing count 
print(count)




'''Loop from end to start using a negative step in slice (i.e. [::-1]), and print reversed "12345".'''
# making variable counting
counting = "12345"
# directly looping in new line each character in a variable lets target variable counting
for lets in counting[::-1]:
    print(lets)

# making a container for holding variables from loop
held = ""
# getting into for loop named straightreverse target variable counting
for straightreverse in counting:
    # held is variable name outside loop, straightreverse is loop name,
    #  and by putting it before held 
    # after = it print in reverse the last variable goto front of the held
    held = straightreverse + held

# now printing variable held
print(held)




'''Write a loop that prints
 a slice of string "abcdefghij" 
 from index 0 to i in each iteration (i from 1 to 10), like:
 a  
ab  
abc  
...  
abcdefghij

 '''

#  making variable ten_times
ten_times = "abcdefghij" 
# checking length of variable with len()
print(len(ten_times)) #10,  but from 0 to 9, # 9
# making a basket for holding loop ietartions and adding one each time in it named as holding
holding = ""
# writing for loop named as _zero target variable ten_times
for _zero in ten_times:
    # in ths line i am really trying to store every iteration in variable holding,
    # and whatever will be stored in holding will go in again for the next character and will add it to the previous one and,
    # so on until end like: loop will print:
    # a
    # b
    # c
    # d
    # here this variable holding will take them as 
    # a
    # a + b = ab
    # ab + c = abc
    holding = holding + _zero
    print(holding)

# just making a variable shrinker targeting ten_times
shrinker = ten_times
# getting into for loop with name reversing targeting shrinker
for reversing in shrinker:
    # printing shrinker the loop will just iterate the whole text
    print(shrinker)
    # using auto feature of python to print the whole line but cutting the last one every time [ : -1]
    shrinker = shrinker[ : -1]






