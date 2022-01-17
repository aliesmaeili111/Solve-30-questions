# What day of the year are we in ?

day , month = map(int , input('Please enter your number :> ').split())


if 1 <= day <= 31 and 1 <= month <= 12:

    if month <= 6 :
        n = ( month - 1 ) * 31 + day
        print(n)
        
    else:
        if month < 11 :
            n = 186 + ( month - 6 ) * 30 + day 
            print(n)
        else:
            if month == 12 :
                n = 336 + day 
                print(n)
else:
    print('\t \t \n " Please enter the day and year correctly " \n ')