from scipy.stats import norm

# probabiltiy/shaded region
shaded_region = 0.2389

# using.ppf method to find the k_value
k_value = norm.ppf(shaded_region)



print(k_value)
