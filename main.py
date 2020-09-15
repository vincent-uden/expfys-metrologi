import numpy as np

from matplotlib import pyplot as plt
from utils import *

P = np.loadtxt('tryckfalt.dat')
u = np.loadtxt('vindfalt_u.dat')
v = np.loadtxt('vindfalt_v.dat')

x = np.linspace(0, 55*30, 31)
y = np.linspace(0, 55*29, 30)

grad = np.gradient(P)
div = divergence(u, v)
crl = curl(u, v)

fig, ax = plt.subplots(2,2)

c = ax[0,0].contourf(x, y, P, 11)
plt.colorbar(c, ax=ax[0,0])
ax[0,0].set_title("Nivåkurvor, lufttryck (hPa)")

ax[0,1].streamplot(x, y, u, v, linewidth=1, density=1)
ax[0,1].quiver(x, y, u, v)
ax[0,1].set_title("Fältlinjer, vindhastighet")

c = ax[1,0].contourf(x,y,div)
plt.colorbar(c, ax=ax[1,0])
ax[1,0].set_title("Divergens, vindhastighet")

c = ax[1,1].contourf(x,y,crl)
plt.colorbar(c, ax=ax[1,1])
ax[1,1].set_title("Rotation, vindhastighet")

plt.show()
