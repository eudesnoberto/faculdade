import matplotlib.pyplot as plt
import numpy as np

# Criar uma figura
fig, ax = plt.subplots(figsize=(8, 6))

# Fundo
ax.set_facecolor('skyblue')

# Torre principal
ax.add_artist(plt.Rectangle((0.45, 0.2), 0.1, 0.4, color='gray'))

# Janelas da torre principal
for y in np.arange(0.3, 0.6, 0.15):
    ax.add_artist(plt.Rectangle((0.46, y), 0.04, 0.05, color='white'))

# Torre secundária
ax.add_artist(plt.Rectangle((0.35, 0.25), 0.1, 0.3, color='gray'))

# Janelas da torre secundária
for y in np.arange(0.3, 0.5, 0.15):
    ax.add_artist(plt.Rectangle((0.36, y), 0.04, 0.05, color='white'))

# Portão
ax.add_artist(plt.Rectangle((0.425, 0.1), 0.15, 0.1, color='brown'))

# Ponte levadiça
ax.add_artist(plt.Line2D([0.5, 0.5], [0.1, 0.2], color='brown', linewidth=3))
ax.add_artist(plt.Line2D([0.425, 0.575], [0.175, 0.175], color='brown', linewidth=3))

# Bandeira no topo da torre
ax.add_artist(plt.Rectangle((0.45, 0.65), 0.1, 0.02, color='red'))
ax.add_artist(plt.Line2D([0.5, 0.5], [0.65, 0.68], color='black', linewidth=2))
ax.add_artist(plt.Circle((0.5, 0.68), 0.005, color='black'))

# Configurações de eixos
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
