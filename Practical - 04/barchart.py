import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 12, 39]

# Create the bar chart
plt.figure(figsize=(8, 4))
plt.bar(categories, values, color='purple')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Sample Bar Chart')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()