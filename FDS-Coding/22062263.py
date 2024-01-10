# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:41:12 2024

@author: USER
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Identify the data file based on the student ID's last digit
# Assuming your student ID's last digit is 3
last_digit = 3
data_file_name = 'data3-2.csv'

# Combine the current directory and file name to create the full file path
full_file_path = os.path.join(current_directory, data_file_name)

# Read the data from the CSV file into a DataFrame
data = pd.read_csv(full_file_path, header=None, names=['Annual Salary'])

# Create a probability density function and plot as a histogram
plt.hist(data['Annual Salary'], bins=30, density=True, alpha=0.6, color='g', label='Histogram (Data)')

# Calculate mean annual salary (W~)
mean_salary = np.mean(data['Annual Salary'])

# Calculate the standard deviation
std_dev = np.std(data['Annual Salary'])

# Create a range of values for the probability density function
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean_salary, std_dev)

# Plot the probability density function
plt.plot(x, p, 'k', linewidth=2, label='Probability Density Function (PDF)')

# Calculate and print the required value X based on the last digit of your student ID
if last_digit == 0:
    x_value = np.percentile(data['Annual Salary'], 25)
elif last_digit == 1:
    x_value = np.percentile(data['Annual Salary'], 33)
elif last_digit == 2:
    x_value = np.percentile(data['Annual Salary'], 5)
elif last_digit == 3:
    x_value = np.percentile(data['Annual Salary'], 33)
elif last_digit == 4:
    x_value = np.percentile(data['Annual Salary'], 25)
elif last_digit == 5:
    x_value = np.percentile(data['Annual Salary'], 10)
elif last_digit == 6:
    x_value = np.percentile(data['Annual Salary'], 0.25 * (1.25 * mean_salary - mean_salary) + mean_salary)
elif last_digit == 7:
    x_value = np.percentile(data['Annual Salary'], 0.25 * (mean_salary - 0.75 * mean_salary) + 0.75 * mean_salary)
elif last_digit == 8:
    x_value = std_dev
elif last_digit == 9:
    x_value = np.percentile(data['Annual Salary'], 0.4 * (1.2 * mean_salary - 0.8 * mean_salary) + 0.8 * mean_salary)

# Plot a vertical line at the calculated X value
plt.axvline(x_value, color='r', linestyle='--', label=f'X Value: {x_value:.2f}')

# Set axis labels, title, and legend for the final graph
plt.xlabel('Annual Salary (Euros)')
plt.ylabel('Probability Density')
plt.title('Histogram with PDF and X Value Marked')
plt.legend()

# Display the final graph
plt.show()
