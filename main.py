import numpy as np

from matplotlib import pyplot as plt

P = np.loadtxt('tryckfalt.dat')
u = np.loadtxt('vindfalt_u.dat')
v = np.loadtxt('vindfalt_v.dat')

x = np.linspace(0, 55*30, 31)
y = np.linspace(0, 55*29, 30)

grad = np.gradient(P)

fig, ax = plt.subplots(2,2)

c = ax[0,0].contourf(x, y, P, 11)
plt.colorbar(c, ax=ax[0,0])
ax[0,0].set_title("Nivåkurvor, lufttryck")
ax[0,1].streamplot(x, y, u, v, linewidth=0.7)
ax[0,1].set_title("Fältlinjer, vindhastighet")
ax[1,0].quiver(x,y,u,v)
ax[1,0].set_title("Vektorfält, vindhastighet")
ax[1,1].quiver(x,y,grad[0],grad[1])
ax[1,1].set_title("Gradient, lufttryck")

plt.show()