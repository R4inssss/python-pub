# Given dataset
data = [1182, 1198, 1215, 1388, 1536, 1612, 1650, 1841, 1904, 2000, 2123, 2151, 2307, 2425, 2425, 2499, 2540, 2625, 2800, 3212]

# Percentile to calculate
percentile = 80

# Calculate the position i for the 80th percentile
n = len(data)
i = ((percentile / 100) * (n)) + 1

# Show calculated index for the 80th percentile

print(i)

# Formula from the "online notes" is i + 1 apparently.
# So, answer is not 2499 but 2540! 
