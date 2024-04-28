# Standard Deviation Python Solver v.1

# Data
print('What is the data?')

data = input()

# a little bit of list comprehention, which we learned the other day
# converts our input (string) as a list of numbers
data = [float(x) for x in data.split()]



# xbar == sigma x / n
mean = sum(data) / len(data)
# takes the sum of squard diff from the mean
square = sum((x - mean) ** 2 for x in data)
# n = length of data
n = len(data)
# stanard deviation
s = (square / (n - 1)) ** 0.5

print(f'The sample standard deviation is: {s}')
print(f'This is your mean: {mean}')
print(f'This is your n: {n}')