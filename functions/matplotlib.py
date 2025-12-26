#MatPlotLib
# AI/ML rapid evolution of genetic permutations of Polymorphic functions at exaflops scale.

import numpy as np
import matplotlib.pyplot as plt

# Generate a range of x values
x = np.linspace(-2, 2, 400)

# Compute the corresponding y values
y = np.exp(x)

# Create the plot
plt.plot(x, y)

# Set the title and labels
plt.title('y = e^x')
plt.xlabel('x')
plt.ylabel('y')

# Display the plot
plt.show()