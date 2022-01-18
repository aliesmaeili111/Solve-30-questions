# salary increase
i = 1

while i <= 2 : 
    number_of_employees = input('Please enter your names :> ')
    old_law = int(input('Please enter your old law :>'))
    
    if old_law <= 25000 : 
        extera_salary = (old_law * 5) / 100
        new_rights = old_law + extera_salary 
        print(f'name : {number_of_employees}')
        print(f'old law: {old_law}')
        print(f'extera_salary : {extera_salary}')    
        print(f'new rights : {new_rights}')   
    if 25000 <= old_law <= 35000 : 
        extera_salary = ((25000 * 5) / 100) + ((35000 - old_law) * 7)/ 100
        new_rights = old_law + extera_salary 
        
        print(f'name : {number_of_employees}')
        print(f'old law: {old_law}')
        print(f'extera_salary : {extera_salary}')    
        print(f'new rights : {new_rights}')  
        
    else:   
        extera_salary = ((25000 * 5) / 100) + ((10000 * 7) / 100)  + ((old_law - 35000) * 10)/100
        new_rights = old_law + extera_salary 
    
        print(f'name : {number_of_employees}')
        print(f'old law: {old_law}')
        print(f'extera_salary : {extera_salary}')    
        print(f'new rights : {new_rights}')    
    i += 1 