import numpy as np
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Параметри інтеграції
a = 0
b = 2
N = 1000000  # Кількість випадкових точок

# Генерація випадкових точок
x = np.random.uniform(a, b, N)
y = f(x)

# Обчислення інтеграла
integral = (b - a) * np.mean(y)
print(f"Оцінка інтеграла методом Монте-Карло: {integral}")

# Перевірка точності з функцією quad
def analytical_function(x):
    return x ** 2

result, error = spi.quad(analytical_function, a, b)
print(f"Точний результат інтеграла: {result}")
