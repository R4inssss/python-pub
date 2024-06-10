import math
import scipy.stats as stats
import sys


class TestMenu:
    def __init__(self):
        options = {
            '1': ContIntZDataSet
        }
        choice = input('Enter your choice: ')
        if choice in options:
            options[choice]()
        else:
            sys.exit()


class ContIntZDataSet:
    def __init__(self):
        stats_summary = data_sets()
        self.display_stats(stats_summary)
        calc_int(stats_summary)

    def display_stats(self, stats_summary):
        print(f'Your sorted data: {stats_summary["sorted_data"]}')
        print(f'The sample standard deviation is: {stats_summary["sample_std_dev"]}')
        print(f'The sample variance is: {stats_summary["variance"]}')
        print(f'This is your range: {stats_summary["range"]}')
        print(f'This is your mean: {stats_summary["mean"]}')
        print(f'This is your n: {stats_summary["n"]}')
        print(f'This is your coefficient variation: {stats_summary["cv"]}%')


def data_sets():
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
    stats_summary = {
        'sorted_data': data_sorted,
        'mean': mean,
        'sample_std_dev': s,
        'variance': s2,
        'range': range_value,
        'n': n,
        'cv': cv,
    }
    return stats_summary


def calc_int(stats_summary):
    print('Enter c (confidence level):')
    conf = float(input())
    z = calc_z(conf)
    mean = stats_summary['mean']
    s = stats_summary['sample_std_dev']
    n = stats_summary['n']
    e = (z * (s / math.sqrt(n)))
    el = mean - e
    eu = mean + e
    print(f'Here is your z-distribution critical value: {z:.4f}')
    print(f'Here is your E: {e:.4f}')
    print(f'Here is your lower E and upper E: {el:.4f} and {eu:.4f}')


def calc_z(confidence):
    alpha = (1 + confidence) / 2
    z = stats.norm.ppf(alpha)
    return z


if __name__ == '__main__':
    TestMenu()
