import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return (x**2 + 1) / 3  # Despeje de x en la ecuación

def fixed_point_iteration(g, x0, tol=1e-5, max_iter=100):
    iterations = [x0]
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        iterations.append(x_new)
        if abs(x_new - x) < tol:
            break
        x = x_new
    return x_new, iterations

# Parámetros iniciales
x0 = 1.5
tolerance = 1e-5

# Aplicamos el método
root, iter_values = fixed_point_iteration(g, x0, tolerance)

# Graficamos la convergencia
x_vals = np.linspace(0, 2, 100)
y_vals = g(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='g(x)')
plt.plot(x_vals, x_vals, '--', label='y = x')
plt.scatter(iter_values, g(np.array(iter_values)), color='red', label='Iteraciones')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Convergencia del método de punto fijo')
plt.legend()
plt.grid()
plt.show()

# Imprimir resultados
print(f"Raíz aproximada encontrada: {root}")
print(f"Número de iteraciones: {len(iter_values)}")
