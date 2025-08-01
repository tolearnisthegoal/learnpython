def collatz(number):
    if number % 2 == 0:
        next_number = number // 2
        
    else:
        next_number = 3 * number + 1
    print(next_number, end=' ')
    return next_number
    
    
num = int(input("Enter an integer: "))
print(num, end=' ')  # Print the starting number

while num != 1:
     num =collatz(num)
        