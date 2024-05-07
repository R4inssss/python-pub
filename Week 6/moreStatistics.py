from scipy.stats import norm
# This program is to find tind the estimated amount of values given mean, sigma, and a value
# our values
mean = 110
sigma = 15
Z1 = 100
# Z2 =
infants = 250

# Z-score
Z = (Z1 - mean) / sigma

# Same thing as ti-83, but cdf via python
# Here, we use P(X <= Xvalue) 
probability = norm.cdf(Z)
# probabilityFor2 = Z2 - Z1
# the estimated number of infants weighing 100 ounces or less 
estimated_infants = probability * infants
# estimatedinfantsFor2 = probabilityFor2 * infants
# rounding

round_baby = round(estimated_infants) # or you can do estimatedinfantsFor2
print(round_baby)
