# Construct a right triangle
a,b,c = map(int,input('Please enter your number :').split())

if a ** 2 == b ** 2 + c ** 2:
    if b ** 2 == a ** 2 + c ** 2 :
        if c ** 2 == a ** 2 + b ** 2 :
            print('We can make a right triangle')
            
else:
    print("We can't make a right triangle")
            