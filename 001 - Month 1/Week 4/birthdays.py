birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information + name')
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

# Here we create the dictionary birthdays
# We make the keys Alice, Bob, and Carol with the pair values being Apr 1, Dec 12
# and mar 4 respectively
# Then we create a while loop using the boolean True value
# We create the variable name, where the variable == the input
# We then create the if condition, where if the name is blank the program exits
# We make another if condition, if the name is in our Dictionary (birthday), it prints
# the dictionary of the input of name + the value pairing of the dictionary
# we then create an else condition, where it prints strings of text to direct the user
# then creates a new variable called bday, where bday = input()
# then it maps the input as a new key pairining in birthday, using the name variable
        