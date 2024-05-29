# Statistics Program v.5
import scipy.stats as stats
import sys
import math


# I made a menu :)
class Statistics:
    def __init__(self):
        options = {
            '1': OneBoundaries,
            '2': Area,
            '3': TwoBoundaries,
            '4': CalculateZ,
            '5': CV,
            '6': MeanZ,
            '7': STDError,
            '8': POPSTDDeviation,
            '9': STDIndividual,
            '10': MarginofError,
            '11': CDFSolver,
            '12': StudentTDistribution,
            '13': ConfidenceIntervalDataSet,
            '14': ConfidenceIntervalNoSet
        }
        print('''Choose an option:
1 = One boundary
2 = Find area for k
3 = Two boundaries
4 = Z-score CDF
5 = CV/STD given set
6 = Mean Z calculation
7 = std error aka sigma subset mean
8 = std deviation
9 = distribution of individuals
10 = margin of error
11 = cumulative distribution of individuals
12 = Student T-distribution
13 = confidence interval given a data set
14 = confidence interval non data set
''')

        choice = input(">>> ")
        if choice in options:
            options[choice]()
        else:
            sys.exit('Choose a valid option.')


# External Functions

# External Function 1, calculate t-distribution
def calc_t(confidence, dof):
    alpha = (1 + confidence) / 2
    t = stats.t.ppf(alpha, dof)
    return t


# Classes
# 1
class OneBoundaries:
    def __init__(self):
        print('What are the variables?')
        print('Mean | Sigma | Z1 | Sample Size')
        mean, sigma, z1, sample_size = map(float, input('>>> ').split())
        z = (z1 - mean) / sigma
        probability = stats.norm.cdf(z)
        estimated_count = probability * sample_size
        variable_rounded = round(estimated_count)
        print(f'Variable rounded: {variable_rounded}')
        print(f'Variable not rounded {estimated_count}')


# 2
class Area:
    def __init__(self):
        print('What is the area for finding k?')
        area = input('>>> ')
        try:
            area = float(area)
            # using.ppf method to find the k_value
            k_value = stats.norm.ppf(area)
            k_value_positive = abs(k_value)
            print(f'k value: {k_value}')
            print(f'k value_positive: {k_value_positive}')
        except ValueError as e:
            print(f'Invalid value {e}')


# 3
class TwoBoundaries:
    def __init__(self):
        print('what are the boundaries lower, upper')
        z_lower, z_upper = map(float, input('>>> ').split())
        # probability using cdf method
        lower = stats.norm.cdf(z_lower)
        upper = stats.norm.cdf(z_upper)
        if lower > upper:
            print('Lower number first, then upper')
        else:
            area_shaded = upper - lower
            print(f'Shaded area: {area_shaded}')


# 4 calculate the cdf
class CalculateZ:
    def __init__(self):
        print('What are the zscores? lower, upper')
        z_lower, z_upper = map(float, input('>>> ').split())
        lower = stats.norm.cdf(z_lower)
        upper = stats.norm.cdf(z_upper)
        print(f'This is your lower: {lower}.')
        print(f'This is your upper: {upper}')


# 5 cv/std deviation given a set of data
class CV:
    def __init__(self):
        print('What is the data? (given a data set)')
        data = input('>>> ')
        data = [float(x) for x in data.split()]
        mean = sum(data) / len(data)
        square = sum((x - mean) ** 2 for x in data)
        n = len(data)
        s = (square / (n - 1)) ** 0.5
        s2 = (square / (n - 1))
        cv = (s / mean) * 100
        mini = min(data)
        maxi = max(data)
        data_sorted = sorted(data)
        range_value = maxi - mini
        print(f'Your sorted data: {data_sorted}')
        print(f'The sample standard deviation is: {s}')
        print(f'The sample variance is: {s2}')
        print(f'This is your range {range_value}')
        print(f'This is your mean: {mean}')
        print(f'This is your n: {n}')
        print(f'This is your coefficient variation: {cv}%')


# 6 Creating standard z using std deviation of sigma(xbar) distribution
class MeanZ:
    def __init__(self):
        print('Given xbar, mu of xbar, and std deviation of xbar.')
        self.xbar, self.mu, self.std = map(float, input('>>> ').split())
        self.calculate_probability()

    def calculate_probability(self):
        print("Enter the lower and upper range for xbar:")
        lower_range, upper_range = map(float, input('>>> ').split())
        z_lower = (lower_range - self.mu) / self.std
        z_upper = (upper_range - self.mu) / self.std
        prob_lower = stats.norm.cdf(z_lower)
        prob_upper = stats.norm.cdf(z_upper)
        probability = prob_upper - prob_lower
        print(f"Z-score for lower range {lower_range}: {z_lower:.4f}")
        print(f"Z-score for upper range {upper_range}: {z_upper:.4f}")
        print(f"Probability that xbar is between {lower_range} and {upper_range}: {probability:.4f}")


# 7, standard error (aka sigma subset mean)
class STDError:
    def __init__(self):
        print('Given std deviation, and sample size.')
        self.std, self.ss = map(float, input('>>> ').split())
        self.calculate_probability()

    def calculate_probability(self):
        deviation = self.std / math.sqrt(self.ss)
        print(f"The standard deviation of the sampling distribution is: {deviation}")


# 8, population standard deviation
class POPSTDDeviation:
    def __init__(self):
        print('Given std deviation, and n.')
        self.xbar, self.n = map(float, input('>>> ').split())
        self.calculate_probability()

    def calculate_probability(self):
        sigma = self.xbar * (self.n ** 0.5)
        print(f"The standard deviation is: {sigma}")


# 9, we do a little copy past from code 1, but iterate it differently.

class STDIndividual:
    def __init__(self):
        print('What are the variables?')
        print('Mean | X | sigma | Sample Size')
        mean, x, sigma, sample_size = map(float, input('>>> ').split())
        z = (x - mean) / sigma
        probability = stats.norm.cdf(z)
        estimated_count = (1 - probability) * sample_size
        variable_rounded = round(estimated_count)
        print(f'Variable (i.e children) given {x} hours: {variable_rounded}')
        print(f'Variable not rounded {estimated_count}')


# 10, margin of error
class MarginofError:
    def __init__(self):
        print('cdf * s/sqrt(n)')
        print('give z(cdf), s, and n')
        z, s, n = map(float, input('>>> ').split())
        moe = z * s / math.sqrt(n)
        print(f'Your margin of error is: {moe}')


# 11 cdf solver
class CDFSolver:
    def __init__(self):
        print('cdf solver v1')
        print('Give x, m, and s')
        x, m, s = map(float, input('>>> ').split())
        answer = ((x - m) / s)
        response = stats.norm.cdf(answer)
        print(f'This is your cdf: {response}')


# 12, student t distribution
class StudentTDistribution:
    def __init__(self):
        print('Enter c (confidence level) and n (sample size):')
        conf, n = map(float, input('>>> ').split())
        df = n - 1
        t = calc_t(conf, df)
        print(f'Here is your t-distribution critical value: {t:.4f}')
        print(f'Here is your degrees of freedom: {df}')


# 13, Confidence interval for mean given unknown
class ConfidenceIntervalDataSet:
    def __init__(self):
        print('What is the data? (given a data set)')
        data = input('>>> ')
        data = [float(x) for x in data.split()]
        mean = sum(data) / len(data)
        square = sum((x - mean) ** 2 for x in data)
        n = len(data)
        s = (square / (n - 1)) ** 0.5
        s2 = (square / (n - 1))
        cv = (s / mean) * 100
        mini = min(data)
        maxi = max(data)
        range_value = maxi - mini
        printing_data = sorted(data)
        print(f'Here is your data{printing_data}')
        print(f'The sample standard deviation is: {s}')
        print(f'The sample variance is: {s2}')
        print(f'This is your range {range_value}')
        print(f'This is your mean: {mean}')
        print(f'This is your n: {n}')
        print(f'This is your coefficient variation: {cv}%')
        print('Enter c (confidence level):')
        conf = float(input())
        print('Is sigma known? (yes/no)')
        sigma_known = input().strip().lower() == 'yes'

        df = n if sigma_known else n - 1
        t = calc_t(conf, df)
        e = (t * (s / math.sqrt(n)))
        el = mean - e
        eu = mean + e
        print(f'Here is your t-distribution critical value: {t:.4f}')
        print(f'Here is your degrees of freedom: {df}')
        print(f'Here is your E: {e:4f}')
        print(f'Here is your lower e and upper e: {el:4f} and {eu:4f}')


# 14, c-interval no data set
class ConfidenceIntervalNoSet:
    def __init__(self):
        print('What is the data? mean, c level, n, ')
        mean, conf, n = map(float, input('>>> ').split())
        print('Is sigma known? (yes/no)')
        sigma_known = input().strip().lower() == 'yes'
        if sigma_known:
            print('What is the sigma?')
            sigma = float(input('>>> '))
            s = sigma
            df = n
        else:
            print('Enter the sample deviation.')
            s = float(input('>>> '))
            df = n - 1

        t = calc_t(conf, df)
        e = (t * (s / math.sqrt(n)))
        el = mean - e
        eu = mean + e
        print(f'Here is your t-distribution critical value: {t:.4f}')
        print(f'Here is your degrees of freedom: {df}')
        print(f'Here is your E: {e:4f}')
        print(f'Here is your lower e and upper e: {el:4f} and {eu:4f}')


if __name__ == '__main__':
    Statistics()
