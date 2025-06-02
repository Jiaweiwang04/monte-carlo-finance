import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


T = 1.0        
N = 1000       
dt = T / N     
t = np.linspace(0, T, N+1)


np.random.seed(42)
#dW = norm.rvs(loc=0, scale=np.sqrt(dt), size=N)
dW = np.random.normal(0,np.sqrt(dt),size=N)  
#W = np.insert(np.cumsum(dW), 0, 0.0)  
W = [0 for i in range(N+1) ]
for i in range(N):
    W[i+1] = W[i] + dW[i]

plt.figure(figsize=(10, 4))
plt.plot(t, W, label="BM Path using scipy.stats.norm")
plt.title("Single Brownian Motion Path")
plt.xlabel("Time")
plt.ylabel("W(t)")
plt.grid(True)
plt.legend()
plt.show()
