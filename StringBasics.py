
double_quote = 'Hi my name is "Ahmad."'
print(double_quote)


tripple_single_quotes = '''Hello
hi
bye
hello
this is what you do by starting and nding a string with tripple quotes'''
print(tripple_single_quotes)

tripple_double_quotes = """hello
you can also do this by tripple double quotes
hi
bye
hello
this is what you do by starting and nding a string with tripple quotes"""
print(tripple_double_quotes)


a = "hello"
b = a[0]    #We are accessing here h
c = a[1]    #We are accessing here e
print(b)
print(c)
# we can aslo print them directly without assigning a variable
print(a[2])   #This is l
print(a[3])   #This is also l



for character in tripple_single_quotes:         #Here Character is my chosen name and in is which variable I want my loop to run
    print(character)


# Create a string
# Assign your name to a variable called my_name and print it.

my_name = "Ahmad"
print(my_name)

# Use single and double quotes
# Create a string like this: I said, "Python is fun" using single quotes around the string.
is_fun = 'I said, "Python is fun"'
print(is_fun)

# Triple quotes multi-line
# Write a multi-line string using triple quotes and print it.
tripe_quote_poem = '''Friends I am here to modestly report
seeing in an orchard
in my town
a goldfinch kissing
a sunflower
again and again
dangling upside down
by its tiny claws
steadying itself by snapping open
like an old-timey fan
its wings
again and again,
until, swooning, it tumbled off
and swooped back to the very same perch,
where the sunflower curled its giant
swirling of seeds
around the bird and leaned back
to admire the soft wind
nudging the bird's plumage,
and friends I could see
the points on the flower's stately crown
soften and curl inward
as it almost indiscernibly lifted
the food of its body
to the bird's nuzzling mouth
whose fervor
I could hear from
oh 20 or 30 feet away
and see from the tiny hulls
that sailed from their
good racket,
which good racket, I have to say
was making me blush,
and rock up on my tippy-toes,
and just barely purse my lips
with what I realize now
was being, simply, glad,
which such love,
if we let it,
makes us feel.
'''
print(tripe_quote_poem)

# Using for to iterate it
for triple in tripe_quote_poem:
    print(triple)

# Check string length
# Use len() to print how many characters are in "Superhuman".
superhuman = "Superhuman"
print(len(superhuman))


# Access individual characters
# Given a = "Python", print the first, third, and last characters.

a = "Python"
print(a[0], a[2], a[5])

# Index out of range
# Try accessing a[10] from the string "cat" and see what happens (handle the error if possible).


'''
cat = "cat"
print(cat[10])
'''

# String indexing practice
# Write a string and print each character one by one using individual index access.
index_practice = "Python."
digit_one = index_practice[0]
digit_two = index_practice[1]
digit_three = index_practice[2]
digit_four = index_practice[3]
digit_five = index_practice[4]
digit_six = index_practice[5]
digit_seven = index_practice[6]
print(digit_one, digit_two, digit_three, digit_four, digit_five, digit_six, digit_seven)
# Using For loop with name variable to iterate from string named index_practice 
for python in index_practice:
    print(python)


# Loop through a string
# Use a for-loop to print each letter in "Banana" both written in straight line with spaces and like list also.

banana = "Banana"
for fruit in banana:
    print(fruit)
    
for another_fruit in banana:
    print(another_fruit, end=" ")
    print()

# Use a different variable name
# Use for x in "Apple" and print x. (Try different variable names.)
vegetables = "Carrots"
for x in vegetables:
    print(x)


# Count vowels
# Count how many vowels are in "Superhumanplanet" using a loop.
sentence = "Superhumanplanet"
vowels = "aeiou AEIOU"
count=0
for human in sentence:
    count = count + vowels.count(human)         #there is a count function for counting things.
print(count)


# Uppercase vowels
# Print only the uppercase vowels from "HeLlO WOrLD".

sent = "HeLlO WOrLD"
vowels1 = "AEIOU"
count1 = 0
for letters in sent:
    count1 = count1 + vowels1.count(letters)

print(count1)

count_this = "n ff,dnlfjnrflfsnd,scfjhfbal"
letter = "f"
count2 = 0
for couting in count_this:
    count2 = count2 + letter.count(couting)
print(count2)


# here in for loop we are using our outside variable and counting it by our own given lett variable which contain what we want to count 
name = "HaseebUllah Ahmad Sami Iqbal"
lett = "aA"
code = 0
for counting in name:
    code = code + lett.count(counting)
print(code)


# Skip spaces
# Use a loop to print only non-space characters from "Hi there, Python coder!".
hi_sentence = "Hi there, Python coder!"
cleaned = hi_sentence.replace(" ", "")
for strip in cleaned:
    print(strip)


# Print with position
# For each character in "Python", print its index and value (e.g., 0 -> P).
pyhton_index = "Python"
print(pyhton_index[0], "0")
print(pyhton_index[1], "1")
print(pyhton_index[2], "2")
print(pyhton_index[3], "3")
print(pyhton_index[4], "4")
print(pyhton_index[5], "5")

# First and last character same?
# Check if the first and last characters of a word (input by user) are the same.
# user_input = input("Enter anything in English ")
# firstdigit_ = user_input[0]
# lastdigit_ =  user_input[-1]
# matching_digit = firstdigit_== lastdigit_
# print("If first digit is equal last digit result will be true otherwise false  \n  Result: ", matching_digit)

# ---------------------------------------------------------------------------------------------------------uncommentme above

# Reverse a string
# Reverse a string using slicing and print it.
text = "Python"
reversed_text = ""

for character in text:
    reversed_text = character + reversed_text  # Adds each new character to the front

print(reversed_text)

# ---------------------------------------------------------------------------------------------------uncomment below
# # Reverse a string
# # Reverse a string using slicing and print it.
# glas = "glass"
# reverse = ""
# for reversed in glas:
#     reverse = reversed + reverse
# print(reverse)

# # String contains a letter
# # Ask the user to input a word. Check if the letter 'e' exists in it.


# word_by_user = input("Enter something in English: ")

# print("e" in word_by_user) 
# #You can search in a string by "in keyword" really just write word like "n" in whatever variable you choosed


# another_word_byuser = input("Enter something in English: ")
# print("j" in another_word_byuser)

# # you can also use .find() it will stop when it will find the first word you want to find nothing more
# wording = input("Enter something in English: ")
# finding = wording.find("e")
# print(finding, "-1 is not found positive number mean found " )

# --------------------------------------------------------------------------------------------------uncomment above


# Count spaces in a sentence
# Count and print how many spaces are in:
# "This is a string with multiple spaces."
counting_spaces = "This is a string with multiple spaces."
blanks = " "
spaces = 0
for blank_spaces in counting_spaces:
    spaces = spaces + blank_spaces.count(blanks)
print(spaces)


# Replace a character manually
# Use a loop to replace every 'a' in "banana" with '*' (without .replace()
character_banana = "banana"
for changing in character_banana:
    print(changing.replace("a", "*"))


# ASCII Art from String
# Write a loop to print each character in a string like this:
# H
# H e
# H e l
# H e l l
# H e l l o

meet = "Hello"
count = ""
for meeting in meet:
    count = count + meeting + " "
    print(count.strip())
    

# Custom separator print
# Given a word like "Python", print each character separated by -. Example: P-y-t-h-o-n

p_y_t = "Python"

_one_ = p_y_t[0]
_two_ = p_y_t[1]
_three_ = p_y_t[2]
_four_ = p_y_t[3]
_five_ = p_y_t[4]
_six_ = p_y_t[5]
print(_one_, _two_,_three_,_four_,_five_,_six_, sep="-")


# Letter frequency
# For "programming", print how many times each letter appears.
p = "programming"
print("p time", p.count("p"))
print("r times",p.count("r"))
print("o times",p.count("o"))
print("g times",p.count("g"))
print("a times",p.count("a"))
print("i times",p.count("i"))
print("n times",p.count("n"))



