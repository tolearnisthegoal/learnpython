# You use a lis when ordering matter but for
# good data or data defining something a dict is a very very good thing

# Ceating a list[]
my_cart = [12.9, 312, 32, 142]
# printing list[]
print(my_cart)



# creating a list[]
container__ = [12.9, 312, 32, 142]
# sum() a list using print()
print(sum(container__)) 


# adding new item to my_cart in my existing list using append()
my_cart.append(39.99)
# printing the updated list
print(my_cart)

# pinting length using len() function of list my_cart
print(len(my_cart))
# accessing 32 from my list 
print(my_cart[2])

# multiplying 32 with 120
print(my_cart[2] * 120)


# making a list[] of strings 
my_items = ["mouse", "laptop", "mic", "screen", "snack"]
# printing my_items
print(my_items)
# printing position [2], in my_items
print(my_items[2])

# printing both of them together
my_products = [my_items,my_items]
print(my_products)



# -----------------------------------------------------------------------------------------
# Dictionaries
# it's like a book
# you look at key and then look at dictionary
# -----------------------------------------------------------------------------------------

my_data = {"name" : "Justin", "location": "California"} # first part name is key and Justin is the definition
print(my_data["name"]) # print Justin
print(my_data.keys()) # give the value of keys with keys()
print(list(my_data.keys())[0])  # printing the element at the key
# adding a new item in dict but .appand() don't work with dict's
my_data["occ"] = "coder" 
# printing data
print(my_data)




# ----------------------------------------------------------------------------------------------
# Practicing
# ----------------------------------------------------------------------------------------------

'''Print each character of "Superman" on a new line.'''
# making variable superman
superman = "Superman"
# initiating a for loop named a targetting superman
for a in superman:
    # printting character by character on new line
    print(a)




'''Create a list of 5 fruits and print the second one.'''
# making a list of fruits 
fruits= ["mango", "apple", "papaya", "orange", "oineapple"]
# now printing the second one
print(fruits[1])

# adding another one in the list
fruits.append("banana")
print(fruits) #printing list

'''Use len() to print how many items are in your fruit list.'''
print(len(fruits)) #should print 6


'''Print the last item in your list using negative indexing.'''
print(fruits[-1]) # should be banana because -1 is always the last one 



'''Multiply the second item in your cart by 5 and print it.'''
print(my_cart[1] * 5) # 1 is the second item it should multiply it with 5




'''Create a list of prices and print their total using sum().'''
# making list as prices
prices = [12, 12.60, 700, 60.89, 300]
# now using the sum and printing result
print(sum(prices))



'''Access the 3rd character from the string "Macbook".'''
# making a string char 
char = "Macbook"
print(char[2])


'''Create a list of 4 subjects you study and print the list.'''
# making a list of subjects
subjects = ["math", "ALgebra", "Physics", "Chemistry"]
print(subjects) # printing the list



'''Make a list of 3 favorite movies and print each one using a loop.'''
# making a list of movies
movies = ["superman", "spiderman", "Avengers"]
# making for loop with name c targetiing movies.
# making a container
cont = ""
for c in movies:
    print(c) #printing movies every one on a new line

# this loop will print them on the same line
for d in movies:
    #this line will print first superman assign it to cont with a space next time add spiderman and space and so on
    cont = cont + d + " " 

print(cont) #printing list on the same line


'''Create a list of ages, and print each age multiplied by 2.'''
# making a list of ages
ages = [10, 23, 45, 3]
# making for loop with name e targetting ages
for e in ages:
    print(e * 2) #this will multiplt ages with 2


'''Create a cart list and print each item price with "Rs." before it.'''
# making rs list
rs = [44, 500, 43, 1000]
# getting into for loop as f targetting rs
for f in rs:
    print("Rs", f)


'''Input 3 prices from the user, store in a list, and print the total.'''
# getting price 1 from user 
price_1 = float(input("Enter price for first item "))
price_2 = float(input("Enter price for second item "))
price_3 = float(input("Enter price for third item "))

#making price list
price_list = [price_1, price_2, price_3]
print(sum(price_list)) # printing price list by adding them in total



'''Create a list of temperatures. Multiply each by 9/5 and add 32 (C to F).'''

# making list of temperatures
temperatures = [33.5, 55.9, 66, 25]
# making a for loog g targeting temperatures
for g in temperatures:
    print((g * 9/5) + 32)


'''Make a list of 4 numbers. Print only the even ones using if.'''
# list of numbers as nos
nos = [4, 5, 8, 9]
# for loop named h targetting nos
for h in nos:
    if h % 2 == 0: # if the remainder of division wih two is zero
        print(h) # then print that number only



'''Count how many items are above 100 in your my_cart list.'''
cart_count = 1 # it's for counting and assigning it, from within the for loop
for j in my_cart:   # getting into loop with j targetting my_cart
    if j > 100: # if number in list is greater than 100 then do whatever the next lines are saying
        print(j, cart_count )   #it will pritn each item on a new line, and its number
        cart_count += 1 # it will increase it by 1 each time

counting = 0    # it's for counting and assigning it, from within the for loop
for k in my_cart: # getting into loop with k targetting my_cart
     if k > 100:    # if number in list is greater than 100 then do whatever the next lines are saying
         counting += 1  # it will increase it by 1 each time
print(counting) # it will just print the number assigned to counting 


'''Join a list of strings using join() like: "laptop, mouse, mic"'''
items = ["biscuits", "baskets", "soaps"] # List of strings
items_join = ", ".join(items)   # Use join() to combine them into one string with commas and spaces
print(items_join)   # Print the result



'''Create a list of 3 items and remove one using .remove()'''
# making list remove_items
remove_items = ["laptop", "mouse", "mic"]
remove_items.remove("laptop")   # removing item "laptop" using .remove()
print(remove_items)     #printing final result, "laptop" shouldn't be here












'''Create a dictionary with name, age, and city. Print all.'''
#dictionary 
dict = {"name ": "Ahmad", "age " : 17, "city ": "Fort"} 
print(dict) #printing whole dictionary


'''Access and print the value of "city" from your dictionary.'''
print(dict["city "])   # printing city which is Fort

'''Print all keys in the dictionary using .keys()'''
print(dict.keys()) # printing keys of dictionary

print(dict.values())    # printing values of dictionary

'''Add a new key "hobby": "gaming" to your dictionary.'''
dict["hobby"] = "gaming"
print(dict) # printing the whole dictionary


'''Create a dictionary of 3 books with their authors.'''
#making dictionary as books
books = {"Think Like a Programmer" : "V. Anton Spraul", "The Art of Problem Solving (AoPS)":"Richard Rusczyk, Sandor Lehoczky", 'Python for Kids: A Playful Introduction to Programming': "Jason R. Briggs"}
print(books)


'''Create a product dictionary: {"mouse": 500, "laptop": 60000}'''

#making dictionary as productts
productts = {"mouse": 500, "laptop": 60000}
print(productts["laptop"] * 2)


'''Add a new item "headphones": 1200 to the product dictionary.'''
productts["headphones"] = 1200
print(productts)

'''Loop through a dictionary and print each key and value.'''  
for m in productts:
    print(m, productts[m]) #m will print keys, and productts[m] will print values



'''Combine a list of item names and a list of prices into one dictionary.'''
list_combine = [productts, my_items]
print(list_combine)


