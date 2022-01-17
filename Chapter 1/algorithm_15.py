# The largest number among 3

a,b,c = map(int,input('Please enter your number :').split())

if a == b or a == c :
    a,b,c = map(int,input('Please enter your number :').split())
if a > b and a > c :
    print(a)
    
if a > b and c > a :
    print(c)
    
if b > a and b > c :
    print(b)

if b > a and c > b :
    print(c)