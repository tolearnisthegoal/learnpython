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


