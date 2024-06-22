from scipy.stats import norm
# This program is to find areas between 2 boundries
# Bounds, P(Z < lower)
Z_lower = -1.2
# Bounds, P(Z < Upper)
Z_upper = 0.9
# So, P(lower, x , upper)

# probabiltiy using cdf method
lower = norm.cdf(Z_lower)
# z 1
upper = norm.cdf(Z_upper)
# z 2
area_shaded = upper - lower

print(area_shaded)
