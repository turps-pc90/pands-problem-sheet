# Weekly Task 8 - plottask.py - a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2 and a plot of the function
# h(x)=x3 in the range [0, 10], on the one set of axes
# Author: Paul Callaghan
# As well as the lecture videos. I researched this task by watching Corey Schafer's Youtube video (https://www.youtube.com/watch?v=XDv6T4a0RNc) on Matplotlib Histograms,
# from GeeksForGeeks guide (https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/)
# and from W3 Schools Matplotlib notes - https://www.w3schools.com/python/matplotlib_intro.asp

import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 values from a normal distribution with mean 5 and standard deviation 2 using NumPy library
data = np.random.normal(5, 2, 1000)

# Plot the histogram and set its properties. Data plots the randomly generated values from NumPy. Bins divides the data into 25 bins or groups.
# Alphas relates to transparency of the bars of histogram. Color 'g' is green. The label for the legend is set to 'Histogram'
plt.hist(data, bins=25, alpha=0.8, color='g', label='Histogram')

# Create x values for the function plot from the NumPy library - 100 equally spaced values between 0 and 10
x = np.linspace(0, 10, 100)
# y is x cubed
#y = x**3

def h(x):
    y = x**3
    return y

# Plot the function and set its properties
plt.plot(x, h(x), color='darkblue', label='h(x) function')

# Set the title, x-label, y-label, and legend
plt.title('Week 8 pands task')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Show the plot
plt.show()