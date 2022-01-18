# Even numbers between 1000 and 2000 and their sum
i , sum = 1000 , 0 
while i < 2000 : 
    print(i , end = " ")
    sum += i
    i += 2 
print(f'\nSum :{sum}')