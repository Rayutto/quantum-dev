#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from qutip import Qobj, basis, qeye, identity, mesolve


# Grid settings
N = 200                  # Number of position points
L = 1.0                  # Length of the well (in arbitrary units)
x = np.linspace(0, L, N) # Position grid
dx = x[1] - x[0]         # Position resolution


# In[7]:


# Construct the finite-difference Laplacian (second derivative)
D2 = -2 * np.eye(N)
for i in range(N - 1):
    D2[i, i+1] = D2[i+1, i] = 1

T = -0.5 * Qobj(D2) / dx**2  # Kinetic energy operator


# In[8]:


V = Qobj(np.diag(np.zeros(N)))  # Potential energy operator


# In[9]:


H = T + V  # Total Hamiltonian

# Get the lowest 5 eigenstates
eigenstates = H.eigenstates()
energies = eigenstates[0]
states = eigenstates[1]

# Print energy levels
print("First 5 energy levels:")
for i in range(5):
    print(f"E{i} = {energies[i]:.4f}")


# In[10]:


plt.figure(figsize=(8, 5))
for i in range(5):
    psi = states[i].full().flatten()
    plt.plot(x, psi / np.sqrt(dx), label=f'n={i+1}')
plt.title("Wavefunctions in Infinite Square Well")
plt.xlabel("Position x")
plt.ylabel("Wavefunction ψ(x)")
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




