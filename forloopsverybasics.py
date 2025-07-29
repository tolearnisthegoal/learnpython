
#  Use when you just want to say or print every character.

# ✅ Easy and useful for: spelling words, reading names, etc.
# -------------------------------------------------------------------------------------------------

for letters in "Python":
    print(letters)
    
''' 
Explain Like I'm 5:
You are walking in a dark tunnel.

You hold a flashlight 🔦.

Each letter is a wall poster.

You can only see one poster at a time with your flashlight.

You don't change the poster. You just look and say it out loud.

# # # # # # 🧠 Why do we use this?

We want to see each thing, like a letter, number, or item, one by one.

Just to observe or show it.'''



# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
'''
Count while looping
 Use this when you want to show numbers with each letter.
'''
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

word = "Dog"
number = 0

for letter in word:
    print("Letter", number, "is", letter)
    number = number + 1
# 🧠 Output:
# Letter 1 is D  
# Letter 2 is o  
# Letter 3 is g
# ✅ Useful for: numbering lines, showing position


# -------------------------------------------------------------------------------------------------------
# “Collect one by one into a box.”
#  Use this when you want to collect all letters into a new string.
# -------------------------------------------------------------------------------------------------------

word = "Hello"
collected = ""
for letter in word:
    collected = collected + letter + " "

print(collected)        #Result = H e l l o

'''
Explain Like I'm 5:
Imagine you have an empty piggy bank 🐖.

Each letter is a coin 🪙.

You put one coin in the piggy bank each time.

collected = collected + letter means:

Take what you already have, and add the new letter to it.

You cannot say letter + collected = ... because Python only lets you assign to the left side of = (like saying “box = old coins + new coin”).
'''


"""
❓ Why do we use + here?
Because we want to add or combine stuff — like gluing letters together.

+ for strings means join them together.
"""

"""
🧠 Why do we use this?
To build a full word, sentence, or pattern bit by bit.

✅ Useful when:
    • Making a new string
    • Fixing something
    • Removing things
(you'll do those later with .replace() or if)
"""


# -------------------------------------------------------------------------------------------------------
# “Know where you are while walking.”  
# -------------------------------------------------------------------------------------------------------

word = "Hi"
for i in range(len(word)):
    print(i, "->", word[i])

'''
Explain Like I'm 5:
You’re walking on a path. Each step has a number.

i is the step number.

word[i] is the letter at that number.

So, step 0 is 'H', step 1 is 'i'.
'''

'''
Why range(len(word))?
range(2) means: 0, 1.

len(word) = how many steps you take.

range(len(...)) is like: “Give me all step numbers for the word.”
'''

# Why do we use this?
# When we need the position (index) of the letter.

# Example: Print every 2nd letter, or skip some letters.


# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# “Make a pattern line by line.”
# Use this when the word should grow line by line like:
# For "Hi":
# H  
# H i
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

text = "Hello"
built = ""
for ch in text:
    built = built + ch + " "
    print(built.strip())


'''
Explain Like I'm 5:
Imagine you're building a tower with blocks.

Each block is a letter.

You place one block at a time.

And every time you place one, you show how the tower looks so far.

The .strip() just cleans the space at the end.
'''

# 🧠 Each time, you add one letter and print what you have so far.
# Why do we use this?
# To create things like:

# H
# H e
# H e l
# H e l l
# H e l l o


# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# “Let only special things pass.”
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

text = "Python Is Cool"
vowels = "aeiouAEIOU"
for ch in text:
    if ch in vowels:
        print(ch)


'''
Explain Like I'm 5:
You’re pouring tea ☕.

A strainer lets only liquid (vowels) pass and blocks leaves (non-vowels).

if ch in vowels: checks if the letter is a vowel.

Only then we print.'''

# Why do we use this?
# To show, skip, or collect only certain items.

# Like only numbers, only uppercase, only spaces, etc.


# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# “Glue things with a connector.”
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

text = "Python"
linked = "-".join(text)
print(linked)

'''
Explain Like I'm 5:
You have 6 beads 🎯: P, y, t, h, o, n.

You want to tie them with a string.

But you also want to put a tiny knot (-) between each bead.

That’s what "-".join(text) does:

Makes it P-y-t-h-o-n.

'''

# Why do we use this?
# To insert something between letters/items.

# Like converting "123" into "1,2,3" or "a b c".



# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# “Flip the order like a mirror.”
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

text = "Python"
reversed = ""
for letter in text:
    reversed = letter + reversed
print(reversed)

'''
Explain Like I'm 5:
You’re lining up toy cars, one by one.

But instead of putting the next one at the end, you put it in the front.

So the first car becomes the last, and the last car becomes the first.
'''

'''
Why letter + reversed, not reversed + letter?
Because we want the new thing to go to the front.

If we do reversed = letter + reversed, it keeps building backwards.
'''

# Why do we use this?
# To reverse a word, number, pattern.














# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
''' Solving Challenges '''
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------


# Print each character in the string "Coding".
letter = "Coding"
for count in letter:
    print(count)

# Challenge 2:
# Print each number in the list [1, 2, 3, 4].

listing = [1, 2, 3, 4]
for list in listing:
    print(list)

# Challenge 3:
# Print each word in this list: ["Python", "is", "fun"].
# Print each letter in this list: ["Python", "is", "fun"].
each_word = ["Python", "is", "fun"]
word_1 = each_word[0]
word_2 = each_word[1]
word_3 = each_word[2]
for one in word_1:
    print(one)

for two in word_2:
    print(two)

for three in word_3:
    print(three)

for words in each_word:
    print(words)


# Challenge 4:
# Print each letter in your name (put your name in a string).

name = "Asad Ullah"
for names in name:
    print(names)

# Challenge 5:
# Print all characters in the word "loop" in UPPERCASE.
in_word = "loop"
for uppercase in in_word:
    print(uppercase.capitalize())

print()

# Challenge 6:
# Count how many characters are in "Elephant" (don’t use len()).

length = "Elephant"
number = 0
for counting in length:
    print(counting, number)
    number = number+1

