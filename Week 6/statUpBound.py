from scipy.stats import norm
# This program is to find the area given only a z upper, with graph to the right
# Bounds, P(Z < lower)
Z_lower = 0
# Bounds, P(Z < Upper)
Z_upper = 1.23
# So, P(lower, x , upper)

# probabiltiy using cdf method
lower = norm.cdf(Z_lower)

upper = norm.cdf(Z_upper)

area_shaded = upper - lower

print(area_shaded)
