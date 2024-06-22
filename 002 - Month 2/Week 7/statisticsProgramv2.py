# Statistics Program v1
from scipy.stats import norm
import sys
import math


# I made a menu :)
class statisticS:
    def __init__(self):
        options = {
            '1': oneBoundaries,
            '2': area,
            '3': twoBoundaries,
            '4': calculateZ,
            '5': cV,
            '6': meanZ,
            '7': stdError,
            '8': populationStdDeviation,
            '9': stdIndividual
        }
        print('''Choose an option:\n1 = One boundary\n2 = Find area for k
3 = Two boundaries\n4 = Z-score CDF\n5 = CV/STD given set\n6 = Mean Z calculation
7 = std error aka sigma subset mean\n8 = std deviation\n9 = distribution of individuals''')

        choice = input(">>> ")
        if choice in options:
            options[choice]()
        else:
            sys.exit('Choose a valid option.')




# 1
class oneBoundaries:
    def __init__(self):
        print('What are the variables?')
        print('Mean | Sigma | Z1 | Sample Size')
        mean, sigma, Z1, sample_size = map(float, input('>>> ').split())
        Z = (Z1 - mean) / sigma
        probability = norm.cdf(Z)
        estimated_count = probability * sample_size
        variableRounded = round(estimated_count)
        print(f'Variable rounded: {variableRounded}')
        print(f'Variable not rounded {estimated_count}')


# 2
class area:
    def __init__(self):
        print('What is the area for finding k?')
        area = input('>>> ')
        # using.ppf method to find the k_value
        k_value = norm.ppf(area)
        print(f'k value: {k_value}')

# 3
class twoBoundaries:
    def __init__(self):
        print('what are the boundaries lower, upper')
        Z_lower, Z_upper = map(float, input('>>> ').split())
        # probabiltiy using cdf method
        lower = norm.cdf(Z_lower)
        upper = norm.cdf(Z_upper)
        if lower > upper:
            print('Lower number first, then upper')
            return False
        else:
            area_shaded = upper - lower
            print(f'Shaded area: {area_shaded}')

# 4 calculate the cdf
class calculateZ:
    def __init__(self):
        print('What are the zscores? lower, upper')
        Z_lower, Z_upper = map(float, input('>>> ').split())
        lower = norm.cdf(Z_lower)
        upper = norm.cdf(Z_upper)
        print(f'This is your lower: {lower}.')
        print(f'This is your upper: {upper}')

# 5 cv/std deviation given a set of data
class cV:
    def __init__(self):
        print('What is the data? (given a data set)')
        data = input('>>> ')
        data = [float(x) for x in data.split()]
        mean = sum(data) / len(data)
        square = sum((x - mean) ** 2 for x in data)
        n = len(data)
        s = (square / (n - 1)) ** 0.5
        s2 = (square / (n - 1))
        cv = (s/mean) * 100
        mini = min(data)
        maxi = max(data)
        range_value = maxi - mini
        print(f'The sample standard deviation is: {s}')
        print(f'The sample variance is: {s2}')
        print(f'This is your range {range_value}')
        print(f'This is your mean: {mean}')
        print(f'This is your n: {n}')
        print(f'This is your coefficient variation: {cv}%')

# 6 Creating standard z using std deviation of sigma(xbar) distribution 
class meanZ:
    def __init__(self):
        print('Given xbar, mu of xbar, and std deviation of xbar.')
        self.xbar, self.mu, self.std = map(float, input('>>> ').split())
        self.calculate_probability()

    def calculate_probability(self):
        print("Enter the lower and upper range for xbar:")
        lower_range, upper_range = map(float, input('>>> ').split())
        Z_lower = (lower_range - self.mu) / self.std
        Z_upper = (upper_range - self.mu) / self.std
        prob_lower = norm.cdf(Z_lower)
        prob_upper = norm.cdf(Z_upper)
        probability = prob_upper - prob_lower
        print(f"Z-score for lower range {lower_range}: {Z_lower:.4f}")
        print(f"Z-score for upper range {upper_range}: {Z_upper:.4f}")
        print(f"Probability that xbar is between {lower_range} and {upper_range}: {probability:.4f}")

# 7, standard error (aka sigma subset mean)
class stdError:
    def __init__(self):
        print('Given std deviation, and sample size.')
        self.std, self.ss = map(float, input('>>> ').split())
        self.calculate_probability()

    def calculate_probability(self):
        deviation = self.std / math.sqrt(self.ss)
        print(f"The standard deviation of the sampling distribution is: {deviation}")

# 8, population standard deviation
class populationStdDeviation:
    def __init__(self):
        print('Given std deviation, and n.')
        self.xbar, self.n = map(float, input('>>> ').split())
        self.calculate_probability()

    def calculate_probability(self):
        sigma  = self.xbar * (self.n ** 0.5)
        print(f"The standard deviation is: {sigma}")
# 9, we do a little copy past from code 1, but iterate it differently.

class stdIndividual:
    def __init__(self):
        print('What are the variables?')
        print('Mean | X | sigma | Sample Size')
        mean, X, sigma, sample_size = map(float, input('>>> ').split())
        Z = (X - mean) / sigma
        probability = norm.cdf(Z)
        estimated_count = (1 - probability) * sample_size
        variableRounded = round(estimated_count)
        print(f'Variable (i.e children) given {X} hours: {variableRounded}')
        print(f'Variable not rounded {estimated_count}')


if __name__ == '__main__':
    statisticS()