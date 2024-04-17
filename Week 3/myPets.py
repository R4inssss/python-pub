myPets = ['Sophie', 'Momo', 'Tammy']

print('Enter a pet name: ')

name = input()

if name not in myPets:
    print('I do not have the pet named: ' + name)

else:
    print(name + ' is my pet.')



