''' Challenge 1: Spell Your Name Letter by Letter'''
# making a name variable
name = "Ahmad"
# getting into loop named as letter targeting name variable
for letter in name:
    # this will print it letter by letter
    print(letter)
    # this will print thee whole name five time,
    # because Ahmed has 5 characters after each character
    print(name)
# getting into loop named as letter targeting name variable
for letter in name:
    # this will print Ahmad five times in a new line every time
    print(name)




'''Add a Sound to Every Letter
Print every letter of the word “Magic”, and after each letter, print "✨" on the same line.
'''
# adding variable sound
sound = "Magic"
# starting a for loop with a variable name magic targeting sound variable
for magic in sound:
    # now printing every letter on a new line with ✨ added to it at the end
    print(magic + "✨")


'''
Print each character of the string "Coding" with its position number.
'''

# creating variable code 
code = "Coding"
# creating a variable numberign int() data-type to count

numbering = 1 # it will start with 1 if i say one here, with 0 if i say so, and with 20 if i say so
# now getting into a for loop with name no targeting code
for no in code:
    print(no, "Number is ", numbering)
    numbering += 1


'''
Label Every Word in a Phrase
🧠 Goal:
Given this phrase: "Code Eat Sleep Repeat"
'''
# variable name Goal
Goal = "Code Eat Sleep Repeat"
# splitting the goal string into words using function .split()
seperating = Goal.split()
# checking the result of split()
print(seperating)
# making a variable coun for counting
coun = 0
# getting into for loop with name a targeting seperating
for a in seperating:
    # printing each word with count, which will just add number as we ietrate
    print(a, coun)
    # adding coun with one with every iteration
    coun += 1



'''
Goal:
Build a dashed version of the word "Fun" using a loop.
Collect each letter into a string, with a dash - after every letter.
result:
F-u-n
'''

# variable fun
fun = "Fun"
# a bucket to hold loop iterated words
words = ""
# getting into for loop with name wor targeting fun
for wor in fun:
    # now this will print every character add - into it with a space " "
    words = words + wor + "-" 
# now printing words and with .rstrip("-") getting rid of last -
print(words.rstrip("-"))


'''Print each character of the word "Rocket" with its index number,
 like you're reading a secret code where every letter has a number.'''

# making variable
rocket = "Rocket"
# making counting_ variable for counting
counting_ = 0
# getting into for loop as b targetting rocket
for b in rocket:
    # it should output each character as 0 ==> R on a new line then again 0==>o until t
    print(counting_, "==>",  b)
    # it will add into variable counting and will increase it from 0 ,1 ,2 so on
    counting_ += 1




'''
Using a loop, print the word "Peace" so it grows line by line like this:

P  
P e  
P e a  
P e a c  
P e a c e
'''

# making variable peace 
peace = "Peace"
# a bucket to hold each iterated character
no = ""
# getting into for loop as c targetting peace
for c in peace:
    # am saying variable no should have each iteration and
    #  add next one into it as iteration grows
    no = no + c + " "
    # now printing no variable output is expected as the expected result
    print(no)
    

