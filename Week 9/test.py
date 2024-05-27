import scipy.stats as stats


class StudentTDistribution:
    def __init__(self):
        print('Enter c and n:')
        conf, n = map(float, input('>>> ').split())
        df = n - 1
        t = self.calc_t(conf, df)
        print(f'Here is your t-distribution critical value: {t:.4f}')
        print(f'Here is your degrees of freedom: {df}')

    def calc_t(self, confidence, dof):
        alpha = (1 + confidence) / 2
        t = stats.t.ppf(alpha, dof)
        return t


if __name__ == '__main__':
    StudentTDistribution()
