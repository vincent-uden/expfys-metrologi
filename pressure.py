import numpy as np

from matplotlib import pyplot as plt
from utils import *

P = np.loadtxt('tryckfalt.dat')

fig, ax = plt.subplots(1,1)

c = ax.contourf(x, y, P, 11)
plt.colorbar(c, ax=ax)
ax.set_title("Nivåkurvor, lufttryck (hPa)")

plt.show()