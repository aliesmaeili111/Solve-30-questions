# The complete number
sum , i = 0 , 1
number = int(input('Please enter your number :>'))
while i <= (number//2):
    r = number - i * ( number//i )
    if r == 0 :
        sum += i 
    i += 1 
    
print(f'{number} The complete number') if sum == number else print(f'{number} The number is not complete')
    
    