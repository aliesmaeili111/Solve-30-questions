# Factorial

number = int(input('Please enter your number :>'))
p , i = 1 , 1
while i <= number : 
    p *= i 
    i += 1 
    
print(f'{number}! = {p}')