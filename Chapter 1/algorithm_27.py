# Numerical algorithm in base 2 and convert it to base 10
number =int(input('Please enter your number :> ')) 
sum , t = 0 , 0 

while number > 0 :
    r = number - (10 * (number // 10))
    sum += r * (2**t)
    number = number // 10
    t += 1
    
print(f' => basis 10 : {sum}')

print(bin(219))