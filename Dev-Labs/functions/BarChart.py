import numpy as np
import matplotlib.pyplot as plt

# Generate a range of x values
x = np.arange(0, 1001)

# Compute the corresponding y values
y = np.exp2(x)

# Create the bar chart
plt.bar(x, y)

# Set the title and labels
plt.title('y = 2^x')
plt.xlabel('x')
plt.ylabel('y')

# Display the plot
plt.show()