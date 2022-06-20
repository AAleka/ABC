import matplotlib.pyplot as plt
from ABC import artificial_bee_colony_optimization
from functions import *
from matplotlib.colors import LogNorm

"""
rosenbrocks: [-100, 100, -100, 100, 250, rosenbrocks, rosenbrocks_f, 1, 1]

sphere: [-100, 100, -100, 100, 250, sphere, sphere_f, 0, 0]

beale: [-4.5, 4.5, -4.5, 4.5, 250, beale, beale_f, 3, 0.5]

goldstein_price: [-10, 10, -10, 10, 250, goldstein_price, goldstein_price_f, 0, -1]

three_hump_camel: [-5, 5, -5, 5, 250, three_hump_camel, three_hump_camel_f, 0, 0]
"""

args = [[-100, 100, -100, 100, 250, rosenbrocks, rosenbrocks_f, 1, 1],
        [-100, 100, -100, 100, 250, sphere, sphere_f, 0, 0],
        [-4.5, 4.5, -4.5, 4.5, 250, beale, beale_f, 3, 0.5],
        [-10, 10, -10, 10, 250, goldstein_price, goldstein_price_f, 0, -1],
        [-5, 5, -5, 5, 250, three_hump_camel, three_hump_camel_f, 0, 0]]

n = input("Rosenbrock: 0\nSphere: 1\nBeale: 2\nGoldstein-Price: 3\nThree Hump Camel: 4\n")

args = args[int(n)]

x = np.linspace(args[0], args[1], args[4])
y = np.linspace(args[2], args[3], args[4])
X, Y = np.meshgrid(x, y)
Z = args[6](X, Y)

fig = plt.figure(figsize=(9, 9))
ax = plt.axes(projection='3d', elev=50, azim=-50)

ax.plot_surface(X, Y, Z, norm=LogNorm(), rstride=1, cstride=1, edgecolor='none', alpha=.8, cmap=plt.cm.jet)
ax.plot(args[7], args[8], args[5]([args[7], args[8]]), 'k*', markersize=10)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')

ax.set_xlim((args[0], args[1]))
ax.set_ylim((args[2], args[3]))
plt.show()

abc = artificial_bee_colony_optimization(target_function=args[5], food_sources=20, iterations=50,
                                         min_values=[args[0], args[2]], max_values=[args[1], args[3]], employed_bees=20,
                                         outlookers_bees=20, limit=40)

result = f"The optimal value has been found: f(x1, x2)={round(abc[2], 5)}, x1={round(abc[0], 5)}, x2={round(abc[1], 5)}"
print(result)

print(f"Global optima: f(x1, x2) = {args[5]([args[7], args[8]])}, x1 = {args[7]}, x2 = {args[8]}")