# s = 1! + 2! + 3! + ... + N!

number = int(input('please enter your number :>'))
sum , t = 0 , 1 

while t <= number :
    p , i = 1 , 1
    while i <= t:
        p *= i 
        i += 1 
    sum += p 
    t += 1 
    
print(f' Sum : {sum}')