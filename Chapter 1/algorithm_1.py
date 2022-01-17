n = int(input("Please enter your number :"))
i,s = 1, 0
while i <= n:
    if n % i == 0 :
        print(i,end= " ")
        s += i 
    i += 1 
print(f"\n sum is : {s}")
