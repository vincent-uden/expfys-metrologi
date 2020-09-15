import numpy as np

from matplotlib import pyplot as plt
from utils import *

p = np.loadtxt('tryckfalt.dat')
u = np.loadtxt('vindfalt_u.dat')
v = np.loadtxt('vindfalt_v.dat')

fig, ax = plt.subplots(1,1)

ax.set_xlim(left=0, right=1650)
ax.set_ylim(bottom=0, top=1595)
ax.set_xlabel("Väster till öster position (km)")
ax.set_ylabel("Sydlig till nordlig position (km)")
ax.streamplot(x, y, u, v, linewidth=0.7, density=1)
ax.set_title("Fältlinjer, vindhastighet")

plt.show()