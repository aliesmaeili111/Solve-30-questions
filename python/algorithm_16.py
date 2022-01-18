# Pairing a number

number = int (input('Please enter your number :>'))

r = number - 2 * (number//2)
if r == 0 :
    print(f'{number} Even number')
else:
    print(f'{number} Odd number')