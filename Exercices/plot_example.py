#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qutip import coherent, wigner
import matplotlib.pyplot as plt
import numpy as np


# In[20]:


alpha = 1.0
dim = 50
xvec = np.linspace(-5, 5, 100)

rho = coherent(dim, alpha)
W = wigner(rho, xvec, xvec)


# In[21]:


plt.contourf(xvec, xvec, W, 100, cmap='magma')
plt.title("Wigner function of |α⟩")
plt.xlabel("Re(α)")
plt.ylabel("Im(α)")
plt.colorbar()
plt.show()


# In[ ]:




