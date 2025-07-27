# Explicit Type Casting
a = "10"
b = "11"
print(int(a) + int(b))


# Implicit type casting
c = 8.9
d = 9
print(c+d)

# Convert the string "100" to an integer and add 50. Print the result.
hundred = "100"
print(int(hundred) + 50)

# Multiply a float 3.5 and an integer 2, print the result and its type.
float3_5 = 3.5
integer2 = 2
multiplyint_float = float3_5 * integer2
print(type(multiplyint_float), multiplyint_float, sep=("   "))

# Convert the string "9.81" to a float, then add it to 10.
c_to_float = "9.81"
print(float(c_to_float) * 10)

# Take a = "True" and try converting it to a boolean using bool(). Print result.
a = "True"
b = bool(a)
print(type(b))
print(bool(a), type(a)) #Type changes if i manually introduce a new variable in print function it doesn't
print(type(a)) # Showing type <str>

# Concatenate two integers 1 and 2 as strings and print.
a = 1
b = 2
print(str(a) + str(b))

# What will be the result and type of this? print(3 + 4.0)
# float type result = 7.0
print(type(3 + 4.0), 3+4.0)

# Convert hex(255) to its string version and print.
color = hex(255)
change_to_string = str(color)
print(color, type(color))

# Convert string "21abc" to int 
# can't it's an error
abc21 = "21abc"
# print(int(abc21))   ValueError: invalid literal for int() with base 10: '21abc'

# Add a float "3.14" (as a string) and integer 4 after converting correctly.
stringasfloat = "3.14"
integer = 4
print(float(stringasfloat) + integer)
print(stringasfloat + str(integer))


# Convert an integer to string, then back to int. Show both conversions.
integerconvert = 14
convert1 = str(integerconvert)
print(type(convert1))

convert2 = int(convert1)
print(type(convert2))

# Take a = "12", b = "6". Divide them after converting to integers.
a = "12"
b = "6"
print(int(int(a) / int(b))) # why it converted to float when am specifically converting to int print(int(a) / int(b))

# Multiply 5 by boolean True and explain the output.
booleantrue = 5
print(booleantrue * True) # booleanTrue is 5, value of True is 1 so 5 * 1 = 5

# Check what int(True) and int(False) returns.
print(type(int(True)))
print(type(int(False)))

# Use float() to convert "10" and add it to 5.5. Print and explain.
tentoconvert = "10"
print(float(tentoconvert) + 5.5)

# Convert string "3.14159" to float, then to integer. Print both results.
converting = "3.14159"
tofloat = float(converting)
print(type(tofloat), tofloat)

toint = int(tofloat)
print(type(toint), toint)


# If a = 5, b = 2.5, Python adds them. What is the type of result?
# result is float 7.5
a = 5
b = 2.5
print(a + b)

# Convert list [1, 2, 3] to string and print it.
listis = [1, 2, 3]
tostring = str(listis)
print(type(tostring), tostring)

# Create a tuple from string "ABC" using tuple(). What will be the result?

stringto = "ABC"
totuple = tuple(stringto)
print(totuple)

# Convert dictionary {"a": 1, "b": 2} to string and print its type.
dictiooonary ={"a" : 1, "b" : 2}
tostringdic = str(dictiooonary)
print(type(tostringdic), tostringdic)

# Can you convert string "False" to bool()? What’s the result?
falsestring = "False"
tobool = bool(falsestring)
print(type(tobool), tobool)

# What happens when you convert "" (empty string) to bool()?
emptystring = ""
emptytobool = bool(emptystring)
print(emptystring) #nothing other than empty space 
