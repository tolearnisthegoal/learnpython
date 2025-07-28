
# Printing default print fucntion without type casting, the default input, the input() function takes from use is str()
a = input("enter any number")
b = input("enter any number")
print(a + b)


# Now overriding the default input() function, by typecasting
c = int(input("enter number: "))
d = int(input("enter number: "))
print(c+d) 

# Again in another way
c = input("Enter Number Please: ")
d = input("Enter any Number: ")
print(int(c) + int(d))

# Now an int() + a str(), remeber this as instructor asked
e = int(input("Enter any number"))
f = int(input("Enter Name"))
print(e + f)


# Ask the user for their name, and print: Hello, <name>!
name = input("Enter you name: ")
print("Hello", name , "!")

# Ask the user for their age, and print: You are <age> years old.
age = int(input("Enter you age in numbers: "))
print("Your are", age, "old.")



# Ask for two words (first and last name), and print them on one line: Full name: <first> <last>
firstname = input("First Name: ")
secondname = input("Second Name: ")
print("Full Name", firstname + secondname)

# Ask the user to type anything, and print the length of the input.
lengthofstring = input("Enter anything for knowing no of Characters: ")
print(len(lengthofstring))

# Ask the user their city and country and print: You live in <city>, <country>
city = input("What City you live in: ")
Country= input("What Country you live in ")
print("You live in", city,Country)

# Ask the user for two numbers and add them together (use int()).
number1 = input("Enter any number: ")
number2 = input("Enter any number: ")
print(int(number1) + int(number2))

# Ask for two decimal numbers and multiply them (use float()).
float_number1 = input("Enter any number with decimal: ")
float_number2 = input("Enter any number with decimal: ")
print(float(float_number1) * float(float_number2))

# Ask for a number and print: That number times 5 is: ___
times_number = input("Enter any number: ")
print(int(times_number) ** 5)

# Ask the user to input their birth year, and print their approximate age.
current_year = 2025
birth_year = input("Enter Year of Your Birth: ")
print(current_year - int(birth_year))


# Ask the user how many apples they have and how many more they want. Print total apples.
how_many_apples_have = input("Enter the amount of apples you have: ")
how_many_more = input("Enter how many more: ")
print(int(how_many_apples_have)+int(how_many_more))

# Ask for two numbers and print which one is greater.
number11 = input("Enter number: ")
number22 = input("Enter number: ")
print("This number is greater than the other", max(int(number11), int(number22)))

# Ask for two numbers and print their difference.
dif_number1 = int(input("Enter any number: "))
dif_number2 = int(input("Enter any number: "))
print(dif_number1 - dif_number2)

# Ask for a temperature in Celsius, and convert it to Fahrenheit: F = (C × 9/5) + 32
Celsius = float(input("Enter temperature in Celsius "))
fahrenheit = (Celsius * 9/5) + 32
print(fahrenheit)

# Ask for distance in kilometers and convert it to miles.
kilometers = float(input("Enter distance in km: "))
miles = kilometers * 0.62137
print("Distance in miles",miles)


# Ask the user how much money they have and check if it’s more than 100.
user_money = int(input("Enter the amount of money you have: "))
limit = 100
check = user_money > limit
print(" True if more than 100, False if less than hundred, Result:",check)

# Ask the user for a noun and a verb. Create a sentence like: "The <noun> loves to <verb>."
noun = input("Enter Noun ")
verb = input("Enter Verb ")
print("The", noun, "loves to", verb)

# Ask the user for a quote and the person who said it. Print it like:
# "<quote>" - <person>
quote = input("Quote ")
person = input("Person ")
print(quote, person)

# Ask the user for three favorite foods, and print them as a bullet list.
fruit1 = input("Enter fav fruit" )
fruit2 = input("Enter fav fruit" )
fruit3 = input("Enter fav fruit" )
print(fruit1)
print(fruit2)
print(fruit3)


# Ask the user to input a 3-digit number and print the sum of its digits.
threedigitnumber = input("Enter 3 digit number ")
digit1 = int(threedigitnumber[0])
digit2 = int(threedigitnumber[1])
digit3 = int(threedigitnumber[2])

print("Sum of three digits is", digit1 + digit2 + digit3)




# Build a simple calculator:
# Ask the user to enter:
# First number
# Operator (+, -, *, /) excluded, i haven't learned if else
# Second number
# Then perform the operation and print the result.


numberoc = int(input("Enter any number: "))
numberoc2 = int(input("Enter any number: "))
print("Addition:", numberoc + numberoc2)
print("Subtraction:", numberoc - numberoc2)
print("Multiplication: ", numberoc * numberoc2)
print("Division:", numberoc / numberoc2)


# Ask user to enter minutes, then print how many seconds that is.
# Hint: 1 minute = 60 seconds
minutes = int(input("Enter Minutes: "))
print(minutes * 60)

# Ask user to enter a number
# Print its square and cube
square_cube = float(input("Enter a number: "))
print("Square is:", square_cube ** 2, "Cube is:", square_cube ** 3)

# Ask user to enter 3 numbers
# Print their average
number__1 = float(input("Enter Number: "))
number__2 = float(input("Enter Number: "))
number__3 = float(input("Enter Number: "))
print((number__1 + number__2 + number__3) / 3)


# Ask user for product price
# Add 18% tax and print total price
# (Don't use if/else, just math)
number__price = float(input("Enter Number: "))
tax = number__price * 0.18
total_tax = tax + number__price
print("After tax:", total_tax)


# Ask user for two numbers
# Print True if they are equal, otherwise False
# Use == operator only
num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
num3 = num1 == num2
print("True if two numbers are equal Result =", num3)

# Input: "45" → Output: 4 + 5 = 9
# Use string indexing: number[0], number[1]
twonumber = input("Enter number: ")
no1 = int(twonumber[0])
no2 = int(twonumber[1])
print(no1 + no2)
