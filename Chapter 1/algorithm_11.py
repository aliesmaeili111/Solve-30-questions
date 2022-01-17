# Triangle construction algorithm
a,b,c = map(int,input('Please enter your number :').split())
if a <= b + c : 
    if b <= a + c : 
        if c <= a + b :
            print('We can make a triangle')
else:
    print("We can't make a triangle")