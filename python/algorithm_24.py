# s = 1/2 - 2/3 + 3/4 - 4/5 + ... + (n-1)/n

number = int(input('please enter your number :>'))


sum , i , k = 0 , 1 , 1 

while i <= number :
    k = k * (-1)
    sum +=  k * (i / (i+1))
    i += 1 
    
print(f'\n Sum : {sum}')