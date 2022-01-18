# The sum of the divisors and their number as well as the sum

# number = int(input('Please neter your number :>'))

# i , sum , count = 1 , 0 , 0 
# while i <= number : 
#     r = number - i *  (number //i )
#     if r == 0 :
#         print(i , end = " ")
#         sum += i 
#         count += 1
#     i += 1 
    
# print(f'\nThe sum of the divisors : { sum }')

# print(f'\n their number as well as the sum : {count}')

# A more efficient method

number = int(input('Please neter your number :>'))
print(1,end = " ")

i , sum , count = 2 , number + 1 , 2

while i <= number//2 : 
    r = number - i *  (number //i )
    if r == 0 :
        print(i , end = " ")
        sum += i 
        count += 1
    i += 1 
    
print(f'\nThe sum of the divisors : { sum }')

print(f'\n Their number as well as the sum : {count}')
