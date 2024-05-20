# Sandwich Maker v1
import pyinputplus as pyip
import sys

# Used the same menu as my statistics program
class Menu:
    def __init__(self):
        print('Make your sandwich using our menu!')
        options = {
            '1': Bread,
            '2': Protien,
            '3': Cheese,
            '4': Condiments
        }
        print('1: Bread\n2: Protein\n3: Cheese\n4: Condiments')
        choice = input("Choose a category or type 'exit' >>> ")
        if choice in options:
            options[choice]()
        elif choice.lower() =='exit':
            sys.exit('No sandwich?')
        else:
            print('Choose a valid option.\n' * 3)
            self.__init__()

# Using inputMenu() for a bread type: wheat, white, or sourdough.

class Bread:
    def __init__(self):
        self.type = {1: 'wheat', 2: 'white', 3: 'sourdough'}
        print('Choose your bread: ')
        response = pyip.inputMenu(list(self.type.values()), numbered=True)
        self.choice = response
        print(f'You chose {self.choice} bread.\n')


# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu
class Protien:
    def __init__(self):
        self.type = {1: 'chicken', 2: 'turkey', 3: 'ham', 4: 'tofu'}
        print('Choose your protien: ')
        response = pyip.inputMenu(list(self.type.values()), numbered=True)
        self.choice = response
        print(f'You chose {self.choice} SCHMEET.\n')



# Using inputYesNo() to ask if they want cheese.
# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
class Cheese:
    def __init__(self):
        want_cheese = pyip.inputYesNo('Do you want cheese? (yes or no): ')
        if want_cheese == 'yes':
            self.type = {1: 'cheddar', 2: 'Swiss', 3: 'mozzarella'}
            print('Choose your cheese:')
            response = pyip.inputMenu(list(self.type.values()), numbered=True)
            self.choice = response
            print(f'You chose {self.choice} cheese.\n')
        else:
            self.choice = 'no cheese'
            print('No cheese selected.\n')

# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
class Condiments:
    def __init__(self):
        self.condiments = []
        condiments_list = ['mayo', 'mustard', 'lettuce', 'tomato']
        for condiment in condiments_list:
            want_condiment = pyip.inputYesNo(f'Do you want {condiment}? (yes or no): ')
            if want_condiment == 'yes':
                self.condiments.append(condiment)
        print(f'You chose the following condiments: {", ".join(self.condiments)}\n' if self.condiments else 'No condiments selected.\n')



# TODO: calculate the cost, since they need to pay :)
# 

# TODO: Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.



if __name__ == '__main__':
    Menu()



# General Goal:
# Write a program that asks users for their sandwich preferences
# Come up with prices for each of these options, and have your program display 
# a total cost after the user enters their selection