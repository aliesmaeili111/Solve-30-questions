# Number of digits of a number
    
number = int(input("Please enter your number :> "))
count , sum= 0 , 0

while number > 0 :
    r = number - ( 10 * (number //10) )
    sum += r
    count += 1 
    number = number // 10
    
print(f' Sum of digit : {sum} and count : {count}')