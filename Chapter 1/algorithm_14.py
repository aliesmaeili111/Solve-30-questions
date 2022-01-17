# The largest number between two numbers

a,b = map(int,input('please enter your number :').split())

if a == b :
    a,b = map(int,input('please enter your number :').split())

if a > b :
    print(f"{a} The largest number and {b} The smallest number")
else:
    print(f'{b} The largest number and {a} The smallest number')