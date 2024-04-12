import matplotlib.pyplot as plt
import numpy as np

# Given salary data in thousands of dollars, excluding the outlier
salaries = [54, 55, 55, 57, 57, 59, 60, 65, 65, 65, 66, 68, 68,
            69, 69, 70, 70, 70, 75, 75, 75, 75, 77, 82, 82, 82,
            88, 89, 89, 91, 91, 97, 98, 98]

# Class boundaries for the histogram without the outlier
class_boundaries = [53.5, 62.5, 71.5, 80.5, 89.5, 98.5]

# Creating the histogram with the specified class boundaries
plt.hist(salaries, bins=class_boundaries, edgecolor='black')

# Set the title and labels
plt.title('Histogram of Employee Salaries')
plt.xlabel('Annual Salaries (in thousands)')
plt.ylabel('Number of Employees')

# Show the plot
plt.show()
