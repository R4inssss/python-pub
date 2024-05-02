# input validator


while True:
    print('Input Age:')
    age = input()
    if age.isdecimal():
        print(f'your age is {age}')
        break
    print('Please enter a number for your age.')


while True:
    print('Select a new password (letters and numbers only): ')
    password = input()
    if password.isalnum():
        print(f"HERE'S  YOUR PASSWORD IN PLAIN TEXT: {password}")
        break
    print('Passwords can only have letters and numbers.')


# Here, we create 2 while loops
# while the first loop is true, it ask for the age, if the age is a decimal it prints and breaks the loop
# moving to the second loop
# if this loop is true, with the password being only alphanumericals using it .isalnum method, it breaks and prints your password
# if it is not true, they print out their respective errors.