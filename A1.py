import matplotlib.pyplot as plt
import numpy as np
__author__ = 'Bolun'

N = 1000000
X = [np.random.uniform(0, 1) for i in range(N)]      #Testing attention please
fig = plt.figure()
ax = fig.add_subplot(111)
plt.hist(X, normed=1)
plt.title("U(0,1) Density Demo")
plt.xlabel("X", fontsize = 16)
plt.ylabel("Density", fontsize=16)
plt.axis([0, 1, 0, 2])

plt.text(.1, .9, 'N = %d' %N, fontsize = 16, transform = ax.transAxes)

plt.savefig('unif-0-1-density.pdf', format = "pdf")
plt.show()