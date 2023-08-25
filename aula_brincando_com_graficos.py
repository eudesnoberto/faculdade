import matplotlib.pyplot as plt
import numpy as np

# Exemplo de dados para o gráfico de linha
x_line = np.linspace(0, 10, 100)
y_line = np.sin(x_line)

# Exemplo de dados para o gráfico de dispersão
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# Criar um gráfico de linha
plt.figure(figsize=(8, 4))  # Tamanho da figura
plt.plot(x_line, y_line, label='Seno(x)')
plt.title('Gráfico de Linha')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()  # Mostra as legendas
plt.grid(True)  # Adiciona uma grade
plt.show()

# Criar um gráfico de dispersão
plt.figure(figsize=(6, 6))  # Tamanho da figura
plt.scatter(x_scatter, y_scatter, color='red', marker='o', label='Pontos Aleatórios')
plt.title('Gráfico de Dispersão')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
