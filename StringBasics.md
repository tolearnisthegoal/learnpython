Anything that you write in a single or double quotes is a string in Python.
name = "Harry"
friend = "Harry"
Another_friend = "Ahad"
A string is actually a sequence or array of textual data. Strings are used when working with Unicode characters.

double_quote = 'Hi my name is "Ahmad."'
print(double_quote)

tripple_quotes = ''' hello
hi
bye
hello
this is what you do by starting and nding a string with tripple quotes'''

tripple_quotes = "hello
you can also do this by tripple double quotes
hi
bye
hello
this is what you do by starting and nding a string with tripple quotes"""


<!-- Assigning Characters of a String -->
In python, String is like an array of characters."Rember not exactly array but like an array of characters". We can access characters of string by using its index which starts from 0.
Square brackets can be used to access the characters of string like:
a = "hello"
b = a[0]    <!--We are accessing here h-->
c = a[1]    <!--We are accessing here e--> 



for character in name:
    print(character)
    <!-- Here Character is my chosen name and in is which variable I want my loop to run -->

<!-- A for-loop is like saying:
like character it can be a x, or an a, or anyword or name of your choice, like a variable
“Go through each item inside this thing, and call it x (or character, or letter, etc.), and do something with it.” -->
<!-- Loop here is just for strings only like this we will learn it later -->

# Count vowels
# Count how many vowels are in "Superhumanplanet" using a loop.
sentence = "Superhumanplanet"
vowels = "aeiou AEIOU"
count=0
for human in sentence:
    count = count + vowels.count(human)         #there is a count function for counting things.
print(count)

