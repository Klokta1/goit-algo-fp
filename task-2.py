import matplotlib.pyplot as plt
import numpy as np

# Функція для малювання гілок дерева Піфагора
def draw_tree(ax, x, y, angle, length, depth, max_depth):
    if depth > max_depth:
        return

    # Обчислюємо кінцеві координати нової гілки
    x_new = x + length * np.cos(angle)
    y_new = y + length * np.sin(angle)

    # Малюємо лінію для цієї гілки
    ax.plot([x, x_new], [y, y_new], color='green', linewidth=1)

    # Рекурсивно малюємо наступні дві гілки
    draw_tree(ax, x_new, y_new, angle + np.pi / 4, length * 0.7, depth + 1, max_depth)  # Ліва гілка
    draw_tree(ax, x_new, y_new, angle - np.pi / 4, length * 0.7, depth + 1, max_depth)  # Права гілка

# Функція для ініціалізації та запуску рекурсії
def pythagoras_tree(level_of_recursion):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Налаштування області малювання
    ax.set_xlim([-10, 10])
    ax.set_ylim([0, 15])
    ax.axis('off')

    # Викликаємо функцію для малювання дерева
    draw_tree(ax, 0, 0, np.pi / 2, 5, 1, level_of_recursion)

    plt.show()

# Запитуємо рівень рекурсії у користувача
recursion_level = int(input("Введіть рівень рекурсії (наприклад, 5): "))
pythagoras_tree(recursion_level)
