Type Casting

Just imagine, we have created a string = "27", if we try to add it into 3 it won't become 30, because 3 is integer, and "27" is string type.
a = "1"
b = "2"
print( 1 + 2 ) result = 12
python is just adding to strings as you asked.

this will look good like this
a = "Ahmad"
b = "Gulfam"
print(a+b)  result = AhmadGulfam 

it's called string concatenation.



The conversion of One data type into another in Python is known as Type Casting.
python support many functions such as int(), list(), tuple() etc.

Two types of type casting:

1 = Explicit Conversion (Explicit type Casting in Python)
2 = Implicit Conversion (Implicit type casting in Python)

Explicit Conversion (Explicit type Casting in Python)
The conversion of one data type into another done via developer as per requirements.
It can be achieved with help of Python built-in functions, such as int(), float(), hex(),oct(), str() etc.

example of explicit conversion is:
    a = "10"
    b = "11"
    print(int(a) + int(b))

if you are coverting into another data type that should be a valid data type as example:
example of explicit conversion is:
    a = "10apple"
    b = "11"
    print(int(a) + int(b))   
    <!-- this is going to give an error as "10apple" is not an integer data type. -->



Implicit Data Type:
    Python convert them auomatically, some of data typr are of higher order so they just over-ride the lower data types

    for example
    c = 8.9
    d = 9
    print(c + d)  result = 17.9
    <!-- in this case result is going to be a float data type because it's of higher order  -->
    Python cnverts a smaller data type into higher data type to prevent data loss.
