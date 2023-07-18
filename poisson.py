import numpy as np
import matplotlib.pyplot as plt

# Generate samples from a poisson distribution
# lamb = 5
# N = 1000

# samples = np.random.poisson(lamb, N)

# Plot the samples

# print(samples)

# plt.hist(samples, bins=10, density=True)
# plt.show()

# Generate a series of uniform random numbers
N = 10
samples = np.random.uniform(0, 1, N)

mean = np.mean(samples)
print(mean)

# calculate the sum of the difference between each sample and the mean
diff = np.sum(samples - mean)
print(samples - mean)
print(diff)


