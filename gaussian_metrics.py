import numpy as np
import matplotlib.pyplot as plt

# In a loop, generate samples from a gaussian with a given standard deviation
mu = 0
sigmas = np.linspace(0.1, 10, 100)
N = 10000

sigma_empiricals = []
mean_deviations = []

for sigma in sigmas:
    samples = np.random.normal(mu, sigma, N)

    # Calculate the empirical standard deviation of the samples
    sigma_empirical = np.std(samples)
    sigma_empiricals.append(sigma_empirical)

    # Calculate the absolute deviation between each sample and the mean
    deviations = np.abs(samples - mu)
    mean_deviation = np.mean(deviations)
    mean_deviations.append(mean_deviation)

# Plot three lines- the empirical standard deviation, the mean deviation, and the theoretical standard deviation
plt.plot(sigmas, sigma_empiricals, label='Empirical standard deviation')
plt.plot(sigmas, mean_deviations, label='Mean deviation')
plt.plot(sigmas, sigmas, label='Theoretical standard deviation')
plt.legend()
plt.show()




