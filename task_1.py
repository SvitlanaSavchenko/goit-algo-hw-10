from pulp import LpMaximize, LpProblem, LpVariable

# Створення задачі
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Створення змінних
lemonade = LpVariable(name="lemonade", lowBound=0, cat='Continuous')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Continuous')

# Обмеження
model += (2 * lemonade + 1 * fruit_juice <= 100, "Water")
model += (1 * lemonade <= 50, "Sugar")
model += (1 * lemonade <= 30, "Lemon Juice")
model += (2 * fruit_juice <= 40, "Fruit Puree")

# Цільова функція
model += (lemonade + fruit_juice, "Total Production")

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Кількість лимонаду: {lemonade.value()} одиниць")
print(f"Кількість фруктового соку: {fruit_juice.value()} одиниць")
print(f"Загальна кількість продуктів: {lemonade.value() + fruit_juice.value()} одиниць")
