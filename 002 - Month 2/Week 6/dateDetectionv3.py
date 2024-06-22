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
# we iterate the first parameters needed
# cool way to do this would to create keys of our months, then iterate the values through the keys
# we know that April, June, September, and November have 30 days, so we can create pairs for them
# the second parameter is for feburary leep days/years, we know that with our inital leep year function
# it will parse if the statement is a leepyear or not, and if it is and it has 28 days then it will pass as true
# else it will return a not boolean statement and pass as another month
# the third parameter is for non leep years for our other months.
# the other months being: Jan/Mar/May/Jul/Aug/Oct/Dec respectively
# with 31 days for each month.
# by iterating this through a dictionary we can map it to the values of day/month/year


# we now need to make our regular expression
# my idea is to use the digit values represented to parse the data
# we can do this with re.compile,
# and use list comprehension to assign the dates
def find_dateas(datea):
    datei = re.compile(r'(\d{2})/(\d{2})/(\d{4})') 
    dates = datei.findall(datea)
    dateb = [date for date in dates if ddmmyyy(int(date[0]), int(date[1]), int(date[2]))]

# use re.compile raw for dd / mm / yyyy given the digits
# iterated through the data using findall
# fun list comprehension, date for date in dates!
# FOR OUR DATES, IN THE DATES IN OUR VARIABLE DATES IT ITERATES THE GROUPS INTO A LIST
# AND CONVERTS EACH STRING INTO AN INTEGER



# Main, we will reuse code because I am lazy and spent too much time on this
# input and sysexit function, with options to call our functions given the values of 1/2
def main():
    print('Input information that needs interating or choose a file.')
    print('Note, dates can only be in DD/MM/YYYY format.')
    print('Select 1 to input from console, select 2 to input from file, or anything else to quit.')
    datec = input(">>> ")
    if datec == '1':
        text = input("Enter text: ")
        dates = find_dateas(text)
        print("Valid dates found:", dates)
    elif datec == '2':
        filepath = input("Enter file path: ")
        with open(filepath, 'r') as file:
            apeed = file.append()
            text = apeed.read()
            dates = find_dateas(text)
            print("Valid dates found:", dates)
    else:
        sys.exit("Goodbye World.")


if __name__ == '__main__':
    main()






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
# Change logs
# added things
#