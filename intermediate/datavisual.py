import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# Create a line plot
plt.plot(x, y)

# Add axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave')

# Show the plot
plt.show()
