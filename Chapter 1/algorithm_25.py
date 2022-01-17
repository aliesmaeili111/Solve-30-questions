# The largest common denominator and the smallest common multiple of two
# |ab| = [a,b] * (a,b) => [a,b] = |ab| / (a,b)

m , n = map (int,input('Please enter your number :> ').split())

if n > m :
    m , n = n , m
    
a , b = m , n 
r = m - ( n * ( m // n ))
if r == 0 :
    print(f'{n} The Greatest Common Divisor')
    
m = n 
n = r
r = m - ( n * ( m // n ))
if r == 0 :
    print(f'{n} The Greatest Common Divisor')
    
kmm = ( a * b ) / n
print(f"\n {kmm} Lowest common multiple")