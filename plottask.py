# plottask.py
# Author : Adedoyinsola Fifo
## plot

import numpy as np
import matplotlib.pyplot as plt
samples = np.random.normal(5, 2, 1000) # Generation of 1000 random numbers with mean of 5 & STD of 2.
fig, ax = plt.subplots()
ax.hist(samples, bins=20, density=True, alpha=0.5, label='Normal Distribution')
x = np.linspace(0, 10, 100)
ax.plot(x, x**3, label='h(x) = x**3')
ax.set_xlabel('x')
ax.set_ylabel('Density')
ax.legend()
plt.show()
