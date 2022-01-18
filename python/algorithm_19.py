# Prime number

number = int(input('Please enter your number:>'))

i = 2
while i < number :
    r = number - i * ( number // i )
    if r == 0 :
        print (f'{number} Is not prime number')  
        break
    i += 1 
else:    
     print(f'{number} Prime number')