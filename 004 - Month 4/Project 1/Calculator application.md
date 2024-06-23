GUI theory:
![[Calculator GUI concept.png]]


# Definitions

```python
# External Function 1, calculate t-distribution  
def calc_t(confidence, dof):  
    alpha = (1 + confidence) / 2  
    t = stats.t.ppf(alpha, dof)  
    return t  
  
  
# External Function 2, calculate z-distribution  
def calc_z(confidence):  
    alpha = (1 + confidence) / 2  
    z = stats.norm.ppf(alpha)  
    return z  
  
  
# External Function 3, Calculate for z using sample mean  
def calc_z_xbar(xbar, mu, s, n):  
    z = (xbar - mu) / (s / math.sqrt(n))  
    return z  
  
  
# External Function 4, Two Tails probability  
def two_tails(z):  
    prob_one_tail = stats.norm.cdf(-abs(z))  
    two_tail_probability = 2 * prob_one_tail  
    return two_tail_probability  
  
  
# External Function 5, proportion SE calculation  
def proportion():  
    print('Enter your variables (n for sample size and p for proportion):')  
    n, p = map(float, input().split())  
    if not (0 <= p <= 1):  
        print("The proportion p must be between 0 and 1.")  
        return  
    if n <= 0:  
        print("The sample size n must be a positive number.")  
        return  
    se = math.sqrt(p * (1 - p) / n)  
  
    print(f'Your standard error is {se:.4f}')  
  
  
# External Function 6, process a data set given the values and standardized names  
def data_sets():  
    print('What is the data? (given a data set)')  
    data = input('>>> ')  
    data = [float(x) for x in data.split()]  
    mean = sum(data) / len(data)  
    square = sum((x - mean) ** 2 for x in data)  
    n = len(data)  
    sx = sum(data)  
  
    while True:  
        print('Population or Sample?')  
        data_type = input('>>> ').strip().lower()  
        if data_type == 'sample':  
            s = (square / (n - 1)) ** 0.5  
            s2 = (square / (n - 1))  
            break  
        elif data_type == 'population':  
            s = (square / n) ** 0.5  
            s2 = (square / n)  
            break  
        else:  
            print('Please enter "population" or "sample"')  
  
    cv = (s / mean) * 100  
    mini = min(data)  
    maxi = max(data)  
    data_sorted = sorted(data)  
    range_value = maxi - mini  
    stats_summary = {  
        'sorted_data': data_sorted,  
        'mean': mean,  
        'std_dev': s,  
        'variance': s2,  
        'range': range_value,  
        'n': n,  
        'cv': cv,  
        'sum x': sx,  
    }  
    return stats_summary  
  
  
# External Function 7, Calculating Interval for Z | Upper/Lower Limits | E value calculation  
def calc_int(stats_summary=None):  
    print('Data set? (yes or no)')  
    response = input('>>> ').lower()  
    if response == 'yes' and stats_summary is not None:  
        try:  
            print('Enter c (confidence level):')  
            conf = float(input())  
            z = calc_z(conf)  
            mean = stats_summary['mean']  
            s = stats_summary['std_dev']  
            n = stats_summary['n']  
            e = (z * (s / math.sqrt(n)))  
            el = mean - e  
            eu = mean + e  
            print(f'Here is your z-distribution critical value: {z:.4f}')  
            print(f'Here is your E: {e:.4f}')  
            print(f'Here is your lower E and upper E: {el:.4f} and {eu:.4f}')  
        except Exception as e:  
            print(f'Error: {e}')  
    elif response == 'no':  
        try:  
            print('What is the data? mean, c level, n, sigma')  
            mean, conf, n, s = map(float, input('>>> ').split())  
            z = calc_z(conf)  
            e = (z * (s / math.sqrt(n)))  
            el = mean - e  
            eu = mean + e  
            print(f'Here is your z-distribution critical value: {z:.4f}')  
            print(f'Here is your E: {e:4f}')  
            print(f'Here is your lower e and upper e: {el:4f} and {eu:4f}')  
        except Exception as e:  
            print(f'Error: {e}')  
    else:  
        print('Invalid response or missing data set.')  
  
  
# External Function 8, calculate for r using Person Correlation Coefficient  
def calculate_r(n, sumx, sumx2, sumy, sumy2, sumxy):  
    numerator = n * sumxy - sumx * sumy  
    denominator = math.sqrt((n * sumx2 - sumx ** 2) * (n * sumy2 - sumy ** 2))  
    r = numerator / denominator  
    return r  
  
  
# External Function 9, sum of squares  
def sum_squares():  
    x = list(map(int, input('>>> ').split()))  
    n = len(x)  
    s = sum(xi ** 2 for xi in x)  
    print(f'Your number of variables: {n}')  
    print(f'Your sum of squares is {s:.4f}')
```

