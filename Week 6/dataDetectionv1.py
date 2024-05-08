# Date Detection v4
import sys
import re



# Task 1 is to calculate Leep Year
# We need it to be every 4 years, not including 100 years and excluding every 400 years)
def isLeep(year):
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Iterating Variables
def ddmmyyy(day, month, year):
    if month in {4, 6, 9, 11} and day <= 30:
        return True
    

    elif month == 2:
        if isLeep(year) and day <= 28:
            return True
        

        elif not isLeep(year) and day <= 28:
            return True
        

    elif month in {1, 3, 5, 7, 8, 10, 12} and day <= 31:
        return True
    

    return False
# Next, we need days, months, and years
# we do this by creating our day, month, and year variable
# we iterate the first parameters needed, which is that 4,6,9,11 need to be 30 days
# the second parameter is for feburary leep years
# the third parameter is for non leep years
# and our final checks are for the rest of the months, with 31 days for each month.
# by iterating this through a dictionary we can map it to the values of day/month/year





# Main
def Main():
    print('Input information that needs interating or choose a file.')
    print('Note, dates can only be in DD/MM/YYYY format.')
    print('Select 1 to input from console, select 2 to input from file, or anything else to quit.')
    choice = input('>>> ')
    if choice == '1':

    elif choice == '2':


    else:
        sys.exit('Goodbye World.')


if __name__ == '__main__':
    Main()






# Todo:
# Used Regex to detect dates in dd/mm/yyyy format
# Assume the days range from 01 - 31
# Months range 01 - 12
# Years range 1000 - 2999
# The regular expression does not have to detect correct days for each month for leap years
# variable names have to be: month, day, and year.
# write additional code that can detect if it is a valid date
# April, June, September, and November have 30 days
# February has 28 days, and the rest of the months have 31 days
# February has 29 days in leap years
# Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is
# also divisible by 400
#
# Let's break it down
# Would it be better to iterate days into months, and months into years
# we can use \d for digits of the dd/mm/yyyy using \d{2} etc
# we also need a way to calculate leep years.
# we know that it needs to be divisible by 4
# we know that it needs to skip years of 100, unless it is 400 years
# we also need to define what is ddmmyyyy in this format
#
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 