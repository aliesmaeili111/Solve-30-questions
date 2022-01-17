# Algorithm s = 1/3^1 + 2/3^2 + 3/3^3 + ... + n / 3^n

number = int(input("Please enter your number : "))
i , sum = 1 , 0

while i <= number : 
    sum += ( i/(3**i) )
    i += 1
    
print(f"Sum:{sum}")

print(1/3 + (2 / (3**2)))