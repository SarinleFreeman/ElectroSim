import pylab as p
from mpl_toolkits.mplot3d import Axes3D
from numpy import asarray, zeros, linspace, sqrt
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

max_x = 100
max_y = 100

delta_x = 1
delta_y = 1

n_x = int(max_x / delta_x)
n_y = int(max_y / delta_y)
N_iter = 70
V = zeros((n_x, n_y), float)
E_x = zeros((n_x, n_y), float)
E_y = zeros((n_x, n_y), float)
for k in range(10, 100 - 10):
    V[k, 20] = 100
    V[k, 80] = 0

for iter in range(70):
    print(f'{iter}')
    for i in range(1, n_x - 2):
        for j in range(1, n_y - 2):
            V[i, j] = 0.25 * (V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1])

for i in range(1, n_x - 2):
    for j in range(1, n_y - 2):
        E_x[i, j] = (V[i + 1, j] - V[i - 1, j]) / 2 * delta_x
        E_x[i, j] = E_x[i, j]
        E_y[i, j] = (V[i + 1, j + 1] - V[i - 1, j]) / 2 * delta_y
        E_y[i, j] = E_y[i, j]


def funcz(V, X, Y):
    z = V[X, Y]
    return z


x = range(0, n_x - 1, 2)
y = range(0, n_x - 1, 2)
mesh_x, mesh_y = p.meshgrid(x, y)
z = funcz(V, mesh_x, mesh_y)
fig = p.figure()
ax = Axes3D(fig)  # Plot axes
ax.plot_wireframe(mesh_x, mesh_y, z, color='r')  # Red wireframe
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential')
p.show()

# vector field
# creating plot.
x = range(0, n_x - 1, 2)
y = range(0, n_x - 1, 2)
mesh_x, mesh_y = p.meshgrid(x, y)
fig, ax = plt.subplots(figsize=(14, 8))
ax.quiver(mesh_x, mesh_y, funcz(E_x, mesh_x, mesh_y), funcz(E_y, mesh_x, mesh_y), color='magenta')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_aspect('equal')
# show plot
plt.show()
