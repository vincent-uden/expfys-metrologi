import numpy as np

def divergence(u, v):
    grad_u = np.gradient(u, 55000)
    grad_v = np.gradient(v, 55000)

    div =  grad_u[0] + grad_v[1]

    return div

def curl(u, v):
    grad_u = np.gradient(u, 55000)
    grad_v = np.gradient(v, 55000)

    curl = grad_v[0] - grad_u[1]

    return curl

x = np.linspace(0, 55*30, 31)
y = np.linspace(0, 55*29, 30)