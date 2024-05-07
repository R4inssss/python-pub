# Statistics Program given Z bound / Area
from scipy.stats import norm
import sys

# 1
class oneBoundaries:
    def __init__(self, boundries):
        self.boundries = boundries
        print('What are the variables?')
        print('Mean | Sigma | Z1 | Sample Size')
        mean, Z1, sigma, sample_size = map(float, input('>>> ').split())
        Z = (Z1 - mean) / sigma
        probability = norm.cdf(Z)
        estimated_count = probability * sample_size
        variableRounded = round(estimated_count)
        
        print(f'Variable rounded: {variableRounded}')
        print(f'Variable not rounded {estimated_count}')


# 2
class area:
    def __init__(self, area):
        self.area = area
        print('What is the area for finding k?')
        area = input('>>> ')
        # using.ppf method to find the k_value
        k_value = norm.ppf(area)
        print(f'k value: {k_value}')

# 3
class twoBoundaries:
    def __init__(self, boundries):
        self.boundries = boundries
        print('what are the boundaries lower, upper')
        Z_lower, Z_upper = map(float, input('>>> ').split())

        # probabiltiy using cdf method
        lower = norm.cdf(Z_lower)
        # z 1
        upper = norm.cdf(Z_upper)
        # z 2
        area_shaded = upper - lower
        print(f'Shaded area: {area_shaded}')



def Statistics():
    print('What kind of statistics?')
    print('1 = one boundary, 2 = area, 3 = 2 boundaries')
    choice = input("> ")
    if choice == '1':
        oneBoundaries()
    elif choice == '2':
        area()
    elif choice == '3':
        twoBoundaries()
    else:
        sys.exit('CHOOSE A BETTER OPTION')

if __name__ == '__main__':
    Statistics()

