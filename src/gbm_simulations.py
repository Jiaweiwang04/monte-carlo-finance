import numpy as np
import matplotlib.pyplot as plt

# Parameters
S0 = 100
mu = 0.05
sigma = 0.2
T = 1
N = 1000
dt = T / N
t = np.linspace(0, T, N + 1)

np.random.seed(10)
Z = np.random.normal(0, 1, N)

# Discrete approximation solution simulation
S_apr = [S0]
for i in range(N):
    S_next = S_apr[-1] * (1 + mu * dt + sigma * np.sqrt(dt) * Z[i])
    S_apr.append(S_next)

# Exact solution simulation
S_exact = [S0]
for i in range(N):
    S_next = S_exact[-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[i])
    S_exact.append(S_next)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, S_apr, label="Discrete Approximation", color='blue')
plt.plot(t, S_exact, label="Exact Solution", color='orange', linestyle='--')
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Comparison of GBM Simulation Methods (Seed=10)")
plt.legend()
plt.grid(True)
plt.show()
