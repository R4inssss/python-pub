# Standard Deviation Python Solver v.2

# Data
print('What is the data?')

data = input()

# a little bit of list comprehention, which we learned the other day
# converts our input (string) as a list of numbers
data = [float(x) for x in data.split()]



# mu == sigma x / N
mean = sum(data) / len(data)
# takes the sum of squard diff from the mean
square = sum((x - mean) ** 2 for x in data)
# N = length of data
N = len(data)
# population standard deviation
m = (square / (N)) ** 0.5

print(f'The population standard deviation is: {m}')
print(f'This is your mean: {mean}')
print(f'This is your n: {N}')

# copy pasting code teehee
