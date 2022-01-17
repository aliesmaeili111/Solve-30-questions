# Read a number one by one and display the largest number between them.

count = int(input('Please enter your number :> '))

a = int(input('Please enter your a :> '))
max , i  = a , 1 

while i < count :
    
    b = int(input('Please enter your b :> '))
    
    if max < b :
        max = b 
        
    i += 1
    
print(f'max : {max}')