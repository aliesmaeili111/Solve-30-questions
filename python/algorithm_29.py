# Name and working hours and hourly wages of office staff
# If the number of hours a worker works is more than 50 hours, add 3/2 hours of salary to its basic salary.

number_of_employees = int(input('Please enter your number :> '))
i = 1 

while i <= number_of_employees : 
    
    name_of_employees = input('Please enter your names :> ')
    number_of_working_hours = int(input('Please enter your number of working hours :> '))
    hourly_wages = int(input('Please enter your hourly wages :> '))
    
    if number_of_working_hours <= 50 :
        s = number_of_working_hours * hourly_wages
        print(f'Name of employees : {name_of_employees} | total rights : {s}')
    else:
        s = 50 * hourly_wages + (number_of_working_hours - 50) * (3/2) * hourly_wages
        print(f'Name of employees : {name_of_employees} | total rights : {s}')
    i += 1 