import scipy.stats as stats
import sys


class testmenu:
    def __init__(self):
        options = {
            '1': StudentTDistribution,
            #'2': CalculateCritT
        }
        choice = input('Enter your choice: ')
        if choice in options:
            options[choice]()
        else:
            sys.exit()


def calc_t(confidence, dof):
    alpha = (1 + confidence) / 2
    t = stats.t.ppf(alpha, dof)
    return t


class StudentTDistribution:
    def __init__(self):
        print('Enter c and n:')
        conf, n = map(float, input('>>> ').split())
        df = n - 1
        t = calc_t(conf, df)
        print(f'Here is your t-distribution critical value: {t:.4f}')
        print(f'Here is your degrees of freedom: {df}')


# class CalculateCritT:
#     def calc_z(self, confidence_level):
#         alpha = (1 + confidence_level) / 2
#         z = stats.norm.ppf(alpha)
#         return z
#
#     confidence_level = 0.96
#     z_critical = calc_z(confidence_level)
#     z_critical_rounded = round(z_critical, 2)


if __name__ == '__main__':
    testmenu()
