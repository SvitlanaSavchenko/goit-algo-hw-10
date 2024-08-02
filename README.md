## Опис домашнього завдання

### Завдання 1. Оптимізація виробництва

Компанія виробляє два види напоїв: "Лимонад" і "Фруктовий сік". Для виробництва цих напоїв використовуються різні інгредієнти та обмежена кількість обладнання. Задача полягає у максимізації виробництва, враховуючи обмежені ресурси.

### Умови завдання:

1. "Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
2. "Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".
3. Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
4. Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
5. Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".

Використовуючи PuLP, створіть модель, яка визначає, скільки "Лимонаду" та "Фруктового соку" потрібно виробити для максимізації загальної кількості продуктів, дотримуючись обмежень на ресурси. Напишіть програму, код якої максимізує загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік", враховуючи обмеження на кількість ресурсів.

### Завдання 2. Обчислення визначеного інтеграла.

Ваше друге завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло.

> [!NOTE]
> INFO
>
> 📖 Можете обрати функцію на власний розсуд.

Виконаємо побудову графіка.

✂️ Це можна запустити!

```python
import matplotlib.pyplot as plt
import numpy as np

# Визначення функції та межі інтегрування

def f(x):
return x ** 2

a = 0 # Нижня межа
b = 2 # Верхня межа

# Створення діапазону значень для x

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка

fig, ax = plt.subplots()

# Малювання функції

ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
```

Отримаємо наступний результат.

![Screenshoot](./image.png)

1. Обчисліть значення інтеграла функції за допомогою методу Монте-Карло, інакше кажучи, знайдіть площу під цим графіком (сіра зона).
2. Перевірте правильність розрахунків, щоб підтвердити точність методу Монте-Карло, шляхом порівняння отриманого результату та аналітичних розрахунків або результату виконання функції `quad`. Зробіть висновки.

> [!NOTE]
> INFO
>
> 📖 Для перевірки обчислення визначеного інтеграла в Python ви можете використовувати бібліотеку SciPy, зокрема її функцію quad з підмодуля integrate. Спочатку необхідно визначити функцію, яку ви хочете інтегрувати, а потім використати quad для обчислення інтеграла на заданому інтервалі.

Приклад застосування функції quad

✂️ Це можна запустити!

```python
import scipy.integrate as spi

# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2

def f(x):
return x**2

# Визначте межі інтегрування, наприклад, від 0 до 1

a = 0 # нижня межа
b = 2 # верхня межа

# Обчислення інтеграла

result, error = spi.quad(f, a, b)

print("Інтеграл: ", result)
```

У цьому прикладі, функція quad повертає два значення: результат інтегрування та оцінку абсолютної помилки.

Виведення:

```python
Інтеграл: 2.666666666666667 2.960594732333751e-14
```

## Критерії прийняття ДЗ

Прикріплені посилання на репозиторій `goit-algo-hw-10` та безпосередньо самі файли репозиторію у форматі `zip`.

### Завдання 1:

Код виконується і повертає максимальну можливу загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік", враховуючи обмеження на кількість ресурсів.

### Завдання 2:

Програмно реалізовано алгоритм пошуку визначеного інтеграла за допомогою методу Монте-Карло. Код виконується та повертає значення інтеграла.

Виконано порівняльний аналіз результату, отриманого за допомогою алгоритму, з результатом, отриманим аналітично або за допомогою функції quad з підмодуля `integrate` бібліотеки `SciPy`.

Зроблено висновки щодо правильності розрахунків шляхом порівняння отриманих результатів і результатів, які дає функція quad або аналітичне обчислення інтеграла. Висновки оформлено у вигляді файлу `readme.md` домашнього завдання.

---

Звісно! Ось приклад пояснень та висновків у форматі Markdown для вашого домашнього завдання.

---

## Пояснення до завдань

## Завдання 1: Оптимізація виробництва

### Опис

У цьому завданні ми вирішили задачу лінійного програмування для максимізації виробництва двох видів напоїв: "Лимонад" і "Фруктовий сік". Ми використали бібліотеку PuLP для побудови математичної моделі, яка враховує обмеження на ресурси та максимізує загальну кількість продукції.

### Результати

- Кількість лимонаду: 30.0 одиниць
- Кількість фруктового соку: 20.0 одиниць
- Загальна кількість продуктів: 50.0 одиниць

### Висновки

- **Кількість лимонаду**: 30 одиниць — це максимальна кількість лимонаду, яку можна виробити при наявних ресурсах.
- **Кількість фруктового соку**: 20 одиниць — це максимальна кількість фруктового соку, яку можна виготовити з доступними ресурсами.
- **Загальна кількість продукції**: 50 одиниць — це максимальна кількість всіх продуктів (лимонаду і фруктового соку) разом, яку можна виготовити при даних обмеженнях.

---

## Завдання 2: Обчислення визначеного інтеграла методом Монте-Карло

### Опис

У цьому завданні ми використовували метод Монте-Карло для оцінки площі під графіком функції \( f(x) = x^2 \) на відрізку від 0 до 2. Ми порівняли результат з аналітично обчисленим інтегралом, щоб перевірити точність методу.

### Результати

- Числовий інтеграл методом Монте-Карло (100 точок): 2.24
- Числовий інтеграл методом Монте-Карло (1000 точок): 2.544
- Числовий інтеграл методом Монте-Карло (10000 точок): 2.7216
- Числовий інтеграл методом Монте-Карло (100000 точок): 2.6616
- Числовий інтеграл методом Монте-Карло (1000000 точок): 2.666224
- Точний результат інтеграла (функція `quad`): 2.666666666666667

### Висновки

- **Метод Монте-Карло**: Результати наближаються до точного значення інтеграла з збільшенням кількості випадкових точок. Це показує, що точність методу підвищується при більшій кількості точок.
- **Малий кількість точок**: Для меншої кількості точок (100, 1000) результати відрізняються від точного значення, але при збільшенні кількості точок (10000 і більше) результат стає ближчим до точного значення.
- **Функція `quad`**: На відміну від методу Монте-Карло, функція `quad` з бібліотеки SciPy надає точний результат з дуже малою помилкою, що підтверджує її ефективність для аналітичного обчислення інтегралів.
