import numpy as np
import matplotlib.pyplot as plt

# Model parameters
eta = 0.05        # long-term mean drift
gamma = 0.5      # speed of mean reversion
sigma = 0.2      # volatility
r0 = 0.1         # initial interest rate
T = 1.0           # total time
N = 1000          # number of time steps
dt = T / N

# Initialize rate array
rates = np.zeros(N + 1)
rates[0] = r0

# Simulate path
for i in range(N):
    phi = np.random.normal()
    rates[i+1] = rates[i] + (eta - gamma * rates[i]) * dt + sigma * phi * np.sqrt(dt)

# Plot result
time = np.linspace(0, T, N + 1)
plt.plot(time, rates)
plt.xlabel("Time")
plt.ylabel("Interest Rate")
plt.title("Interest Rate Path ")
plt.grid(True)
plt.show()
