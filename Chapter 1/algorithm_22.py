# All divisors against numbers between 1 and n .

t = 1

number = int(input('Please enter your number :> '))
while t <= number : 
    print(f' \n{t} ' , end = " : ")
    i = 1 
    while i <= t :
        r = t - i * ( t // i )
        if r == 0 :
            print(i , end = " ")
        i += 1 
    t += 1 