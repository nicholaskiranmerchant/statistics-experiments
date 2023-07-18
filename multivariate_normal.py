import numpy as np
import matplotlib.pyplot as plt

# Generate samples from a 2-dimensional normal distribution
mu = np.array([0,0])
sigma = np.array([[10,0],[0,1]])
N = 100000

samples = np.random.multivariate_normal(mu, sigma, N)

np.exp(2)

# Calculate samples 

# Plot a bell curve
plt.hist2d(samples[:,0], samples[:,1], bins=50, cmap='Blues')
plt.gca().set_aspect('equal', adjustable='box')
# plt.xlim(-10,10)
# plt.ylim(-10,10)

plt.show()

