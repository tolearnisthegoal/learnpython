
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



name = "apple"
num = 0
for len in name:
    print(len, num)
    num = num + 1 


# Challenge 7:
# Print each letter of "Hello" but with a * before it.
hello = "Hello"
for hel in hello:
    print("*", hel)


# Join all letters of "Code" into one string using a loop.
# Expected output:
# Code

code = "code"
container = ""
for contain in code:
    container = container + contain + ""
print(container)


# Challenge 2:
# Count how many vowels are in "Programming" using an accumulator.

# Expected output:
# 3
letters = "Programming"
vowels = "aeiouAEIOU"
counter = 0
for cont in letters:
       if cont in vowels:
           counter += 1
print(counter)


# Sum all numbers in the list [5, 10, 15, 20] using a loop (no sum()).

# Expected output: 50

listing = [5, 10, 15, 20]
addition = 0
for add in listing:
    addition = addition + add
print(addition)


# Challenge 4:
# Reverse this number using a loop: 1234 → 4321 (as a string).

# Hint: Use reversed = digit + reversed

reverse = "1234"
reversing = ""
for rev in reverse:
    reversing = rev + reversing
print(reversing)

# if you just place your variable of for loop behind you global variable or variable outside loop, you get opposite mirrored result
x = "Baba-ba"
c = ""
for y in x:
    c = y + c
print(c)



# Make a sentence from a list: ["I", "love", "Python"]
# Output: I love Python

sen = "I love Python"
sen_count = ""
for count_sen in sen:
    sen_count = sen_count + count_sen
print(sen_count)


# Challenge 6:
# Create a string of only capital letters from "PyTHonIsFuN".

# Expected output:
capitalize = "PyTHonIsFuN"
capital = ""
for cap in capitalize:
    if cap.isupper():
        print(cap)



# Create this pattern using "code":
# c
# c o
# c o d
# c o d e

text_ = "code"
c = ""
for text_count in text_:
    c = c + text_count + " "
    print(c.strip())


# Make a pattern with "abc":
# a
# a b
# a b c

lett = "abc"
lett_count = ""
for count_lett in lett:
    lett_count = lett_count + count_lett + " "
    print(lett_count.strip())


# Create a pattern from "Hi" like this:
# H
# H i

hi = "hi"
hi_count = ""
for count_hi in hi:
    hi_count = hi_count + count_hi + " "
    print(hi_count.strip())

# Build this using "ok":
# o
# o k

ok = "ok"
ok_c = ""
for c_ok in ok:
    ok_c = ok_c + c_ok + " "
    print(ok_c.strip())



# Build a pattern from "loop" with * between each letter:
# l
# l*o
# l*o*o
# l*o*o*p

_star = "loop"
starcount = ""
for countstar in _star:
    starcount = starcount + "*" + countstar
    print(starcount.lstrip("*"))  # You can tell strip function what to remove



# From "wow" build:
# w
# w o
# w o w

wow = "wow"
wow_count = ""
for count_wow in wow:
    wow_count = wow_count + count_wow + " "
    print(wow_count.strip())


# Use "123" and make this pattern:
# 1
# 1 2
# 1 2 3

_123 = "123"
count_123 = ""
for _123count in _123:
    count_123 = count_123 + _123count + " "
    print(count_123.strip())


# Print only vowels from "Hello World"
# Expected:
# e
# o
# o
vowelseoo = "Hello World"
vowels__ = "aeiouAEIOU"
for vow in vowelseoo:
    if vow in vowels:
        print(vow)


# Print only the capital letters from "PyTHonIsCoOL"
# Expected:
# P
# T
# H
# I
# C
# O
# L


upper_ = "PyTHonIsCoOL"
vowels = "aeiouAEIOU"
for capp in upper_:
    if capp.isupper():
        print(capp)


# Skip all spaces and print the rest from "Python is cool"
# Expected:
# P
# y
# t
# h
# o
# n
# i
# s
# c
# o
# o
# l

pythoniscool = "Python is cool"
pythonc = pythoniscool.replace(" ", "")
for pyth in pythonc:
    print(pyth)


# Print only even numbers from this list: [1, 2, 3, 4, 5, 6]
# Expected:
# 2
# 4
# 6

even = [1, 2, 3, 4, 5, 6]
for even_ in even:
    if even_ % 2 == 0:
        print(even_)



# From the word "banana", print only the letter "a" each time it appears.

# Expected:
# a
# a
# a
fruit = "banana"
criteria = "a"
for cri in fruit:
    if cri in criteria:
        print(cri)


print()
print()
print()

# From "I LOVE PYTHON", print only the letters, skip spaces and caps.

# Expected:
# L
# O
# V
# E
# P
# Y
# T
# H
# O
# N

_sentence_ = '"I LOVE PYTHON'
replaced_ = _sentence_.replace('"', "")
_replaced_ = replaced_.replace(" ", "")
I = _replaced_.replace("I", "")
for s in I:
    print(s)


# Challenge 7:
# From "ChatGPT4ever!", print only alphabets, skip digits and punctuation.


text = "ChatGPT4ever!"
for char in text:
    if char.isalpha():     # checks: is this a letter?
        print(char)


# Join "Code" with -
# Expected output: C-o-d-e

join_code = "Code"
joined_ = ""
for _joning in code:
    joined_ = joined_ + _joning + "-"

print(joined_.rstrip("-"))


# Join "Python" with *
# Expected output: P*y*t*h*o*n

join_python = "Python"
jonp = ""
for jo in join_python:
    jonp = jonp + jo + "*"
print(jonp.rstrip("*"))


# Join ["I", "love", "Python"] with a space
# Expected: I love Python
listjoin = ["I", "love", "Python"]
contain_list = ""
for listing in listjoin:
   contain_list = contain_list + listing + " "
print(contain_list )


# Join "AI" with " ❤️ "
# Expected: A ❤️ I

ai = "AI"
heart = ""
for h in ai:
    heart = heart + h + " ❤️  "
print(heart.rstrip(" ❤️ "))


# Manually join "Hi" with ~ using a loop and accumulator
# You must build the result manually, not with .join()
# H~i

hi = "Hi"
h = ""
for n in hi:
    h = h + n + "~"
print(h.strip("~"))

# Join "1234" with a comma
# Expected: 1,2,3,4
l = "1234"
m = ""
for g in l:
    m = m + g + ","
print(m.rstrip(","))


# From "Python", build:

# Python!
# P-y-t-h-o-n!

k = "1234"
p = ""
for w in k:
    p = p + w + "-"
print(p.rstrip("-"), end="!")
print()


joint = "1234"
v = "-".join(joint) + "!"
print(v)



# Reverse the word "code"
# Expected:
# edoc

reverse_code = "code"
codee = ""
for cod in reverse_code:
    codee = cod + codee
print(codee)


# Reverse "Python" using a loop
reverse_python = "Python"
on = ""
for oni in reverse_python:
    on = oni + on
print(on)

# Reverse the number 1234 as a string. Output: "4321"
nume = "1234"
nm = ""
for mn in nume:
    nm = mn + nm
print(nm)

# Reverse only the vowels in "education"
edu = "education"
vow = "AEIOUaeiou"
wo = ""
for ov in edu:
    if vow in vow:
        wo = ov + wo
        print(wo)

# Reverse "Loop Builder" and print each character on a new line, reversed.
looop = "Loop Builder"
loopc = ""
for pc in looop:
    loopc = pc + loopc 

for looping in loopc:
        print(looping)


# Reverse this sentence word-by-word:
# "I love Python"
# expected:
# "Python love I"

wordins = "I love Python"
splitting = wordins.split()

print(splitting)
wordby = ""
for wording in splitting:
    wordby = wording + " " + wordby
print(wordby)