# Algorithm s = 1/2 + 1/4 + 1/6 + 1/8 + ... + 1 / N

number = int(input('Please enter your nubmer :'))

sum , i = 0 , 2

while i <= number : 
    sum += (1 / i)
    i += 2 

print(f'Sum : {sum}')