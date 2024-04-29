# coefficient variation  Solver v.2



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
s2 = (square / (n - 1))
# cv = s/xbar * 100
cv = (s/mean) * 100

# Range of data
mini = min(data)
maxi = max(data)
range_value = maxi - mini

print(f'Given the data: {data}')
print(f'The sample standard deviation is: {s}')
print(f'The sample variance is: {s2}')
print(f'This is your mean: {mean}')
print(f'This is your n: {n}')
print(f'This is your coefficient variation: {cv}%')
print(f'This is your range {range_value}')
