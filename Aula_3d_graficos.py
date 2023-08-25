import matplotlib.pyplot as plt
import numpy as np

# Criação de dados para o gráfico 3D
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')


# Criação do gráfico 3D
ax.plot(x, y, z, label='Curva 3D')
ax.set_title('Gráfico 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
